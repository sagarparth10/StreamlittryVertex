import streamlit as st
import requests
import json
import pandas as pd
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Content, GenerationConfig, HarmCategory, HarmBlockThreshold
import os  # Import the 'os' module

# Streamlit UI
st.title("Video Sentiment Analysis")

video_url = st.text_input("Enter YouTube Video URL:", "https://www.youtube.com/watch?v=Xt8Od-Z78Zs")  # Default video, CHANGE THIS TO YOUR GCS URL
if not video_url:
    st.warning("Please enter a YouTube or GCS video URL.")
    st.stop()

# Vertex AI Configuration
PROJECT_ID = "genai-sandbox-399108"  # Replace with your project ID
LOCATION = "us-central1"  # Replace with your region

# **MODIFIED: Access Service Account Credentials from Streamlit Secrets**
try:
    # 1. Get the credentials directly from Streamlit secrets (assuming it's already parsed)
    credentials_info = st.secrets["VERTEX_CREDENTIALS"]  # No need to load JSON

    # 2. Create credentials from the dictionary.
    credentials = service_account.Credentials.from_service_account_info(credentials_info, scopes=["https://www.googleapis.com/auth/cloud-platform"])

    vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)  # Use credentials here
    st.success("Successfully authenticated with Vertex AI.")

except Exception as e:
    st.error(f"Error authenticating with Vertex AI: {e}")  # Print error e
    st.stop()  # Stop if authentication fails

# Prompt
prompt_text = """
    Provide the full transcript without timeline and Customer Sentiment Summary without timeline in JSON format.
    Ignore any Responsible AI violation part. You are an AI assistant that helps summarize this product's YouTube video transcription.
    Provide the customer sentiment summary with all positives and all negatives sentence based solely on the transcription.
    If there are only negatives, provide only negative points, and if only positives are available, provide only positives.  Rank positives and negatives based on frequency.
    The JSON should include "transcript" and "customer_sentiment_summary" fields. "customer_sentiment_summary" should have "positives", "negatives", and "overall" fields.
    **Do not include any markdown formatting like ```json around the JSON output.**
"""

# Model Configuration
model_name = "gemini-1.5-pro-002"  # Or "gemini-1.5-pro-video" if you have access
model = GenerativeModel(model_name)

generation_config = GenerationConfig(
    temperature=0.7,
    top_p=0.9,
    max_output_tokens=4096  # Adjust as needed.
)

safety_settings = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Analysis Function
def analyze_video(video_url, prompt):
    try:
        content = Content(
            role="user",
            parts=[
                Part.from_uri(video_url, mime_type="video/*"),
                Part.from_text(prompt)
            ]
        )

        responses = model.generate_content(
            [content],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=False  # Important to set to false to get complete JSON
        )

        response_text = responses.text.strip()  # Get the raw text response

        # Debug print
        print("Raw response from Gemini:")
        print(response_text)

        # **Aggressive Cleaning of the JSON Response**
        response_text = response_text.replace("```json", "").replace("```", "").strip() # Remove code blocks
        if response_text.startswith("{"):
          start_index = response_text.find("{")
          response_text = response_text[start_index:]
        if response_text.endswith("}"):
          end_index = response_text.rfind("}")
          response_text = response_text[:end_index + 1]

        try:
            parsed_data = json.loads(response_text)

            transcript = parsed_data.get("transcript", "Transcript not found.")
            sentiment_summary = parsed_data.get("customer_sentiment_summary", {})
            positives = sentiment_summary.get("positives", [])
            negatives = sentiment_summary.get("negatives", [])
            overall_sentiment = sentiment_summary.get("overall", "Overall sentiment not found.")

            return transcript, positives, negatives, overall_sentiment

        except json.JSONDecodeError as e:
            st.error(f"JSON Decode Error: {e}")  # print error message
            st.error(f"Raw response: {response_text}")  # debug
            return None, None, None, None

    except Exception as e:
        st.error(f"An error occurred: {e}")  # print error message
        return None, None, None, None

# Run Analysis
if st.button("Analyze Video"):
    with st.spinner("Analyzing video..."):
        transcript, positives, negatives, overall_sentiment = analyze_video(video_url, prompt_text)

        if transcript:
            st.subheader("Transcript:")
            st.write(transcript)

            st.subheader("Summary:")

            st.write("**Overall Sentiment:**", overall_sentiment)

            if positives:
                st.write("**Positives:**")
                for positive in positives:
                    st.write(f"- {positive}")  # Show items

            if negatives:
                st.write("**Negatives:**")
                for negative in negatives:
                    st.write(f"- {negative}")  # Show items
        else:
            st.warning("Analysis failed. Check the error messages above.")
