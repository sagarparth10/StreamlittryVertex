# # import streamlit as st
# # import requests
# # import json
# # import pandas as pd
# # from google import genai
# # from google.genai import types
# # from google.oauth2 import service_account
# # import vertexai
# # from vertexai.generative_models import GenerativeModel, Part, Content, GenerationConfig, SafetySetting

# # # Define the required scopes
# # scopes = ["https://www.googleapis.com/auth/cloud-platform"]
# # # Load the service account credentials
# # credentials = service_account.Credentials.from_service_account_file(
# #     'C:\\Users\\pxs1101a\\Downloads\\Customer-Feedback-google-oauth\\Customer-Feedback-google-oauth\\SVCCredentials\\marine-actor-449411-t3-9022d9539783.json',
# #     scopes=scopes)


# # # Initialize the client with credentials
# # client = genai.Client(
# #     vertexai=True,
# #     project="marine-actor-449411-t3",
# #     location="us-central1",
# #     credentials=credentials  # Pass the credentials here
# # )

# # # Define the content
# # video1 = types.Part.from_uri(
# #     file_uri="https://www.youtube.com/watch?v=Xt8Od-Z78Zs",
# #     mime_type="video/*",
# # )

# # model = "gemini-2.0-flash-exp"
# # prompt = '''
# #     Can you provide the full transcript without timeline, and Customer Sentiment Summary without timeline in json format?
# #     Ignore any Responsible AI violation part, You are an AI assistant that helps summarize this product's: DCST972X1 YouTube video's transcription. 
# #     Provide the customer sentiment with all positives and all negatives based solely on the transcription. 
# #     Please look at the few examples given below to form your answer, 
# #     NOTE: If there are only negatives then provide only negative points and if only positives are available provide only positives. But if both present include both. Also, rank the positives and negatives based on number of times they appear.
    
# #     for example [please take it as only example and provide your own insights]: 
    
# #     {
# #         "transcript": "Almost a year ago exactly, Dewalt came out with their Flex Bolt Universal attachment string trimmer. Basically, that means this is a 60-volt power head that will take any attachment that is listed as universal. So if it's a universal Ryobi, a universal Dewalt, a universal whatever, it will take that and you'll be able to use it, which is pretty awesome for most people. I have used this as a string trimmer only. I'm going to go through what I deem as what this is really great as after a year, and what it kind of isn't as great as. And we'll go through if you're looking at this at this point in time in the spring, what you might want to consider.\n\nThe Dewalt Flexvolt Universal attachment string trimmer is a 60-volt tool, so it will not take 20-volt batteries. You must be invested in the 60-volt platform. Not a big deal. Small battery, but it does weigh quite a bit because it's 3P. So the balance of this unit is off, although when you're hanging onto it a little differently, it will work a little bit better. With that said, it's a little bit shorter than many, so if you're taller, you might find yourself bending over a little bit more. It's a 15 to 17-inch swath down here on the head end. And the head that's down here, unfortunately, is not always as strong as some of the people using it. If you pound that head against the ground or against rocks, you'll find that it will break quite quickly. It is not expensive to replace with the Dewalt unit and it will take many other units that are out there. It is a speed close head, so you can easily put the line in it, but with that said, beat it against the ground a lot and you'll find yourself with parts laying all over the place. I've got a few friends with these and it happened to them quite quickly and you just have to learn if you're going to keep that head to be fairly gentle with it.\n\nThe second thing that maybe is a little bit annoying to many is going to be the safety. Now, this trigger is probably the most gas-like feeling trigger out there, but actually, it doesn't work anything like a gas trigger. It's a stepped trigger. But with that said, the safety on the top, you have to push this lever over and then hold this down, then you can pull the trigger. Otherwise, it's locked out. Great for throwing it in the back of a truck or something where you're piling it around other things, horrible for actually using it in the yard. Last downside to this is runtime. If you're really pushing this guy, runtimes are about 10 minutes with a 9 amp hour battery. That is like pushing it through solid, heavy grass. If you're just using it in normal household stuff, you can get 20 to 25 minutes out of it.\n\nThe reason why this one landed at my house and not in our contractor trailer or in our lawn mowing trailer is that runtime. Would have to carry two batteries in order to do the same amount of work I could do with a different machine with one battery. Is that because the motor is up top and we have a shaft that runs through? I don't know. There is a lot of power here, although the RPMs are lower. Low is going to be around 4,000 RPMs and high on this is going to max out about 5,800. But with that said, because of the 17-inch swath, you really get some great line speed going and this thing cuts like a beast.\n\nAnd secondly, it is butter smooth. You can use this thing all day if you wanted to and it feels great, it cuts great and there is zero vibrations felt up this grip. This grip is purely Dewalt and once you get over that safety, you will absolutely love it. The stepped trigger most people will get used to it, but when I say stepped trigger, it's not fully variable. It goes in different modes and just watch my finger here and listen.\n\nAs you get closer to the top, it feels more variable, but realistically it's just taking different points and bumping that motor up as it goes. That was not my finger just moving quickly through that. That was the steps as it goes through. Not a big deal. It's a little different than when if you're using gas and you're trying to use the different full variable speeds, it simply doesn't have it. It's just got the steps. Either way, this is one unit that I've kept the 0.080 line on, simply because it works great. A lot of people bump up to the 0.095, I can see why. I do on 99% of my stuff, but around home, I don't feel like I need it and this thing really has great power. And again, the runtime would suffer a little bit more if we upgraded to 0.095 line, so I keep it at 0.08.\n\nNow, kicker of what at home because of the short runtime, I can really do two to three cuts around my yard based off of one battery. I don't need to trim that much, but what ends up happening is the last cut, the third one mostly, the battery is mostly dead and I'll run out of battery. So half the time or a third, two-thirds, whatever, I go out and I'll run this on low only because I'm trying to conserve battery. And around the house on low only, it does awesome.\n\nIt's one of the few units that I actually use the low on because I was forced to because I was kind of a dummy and didn't pull out the battery and charge it up. Overall, this kit here, if you don't need super long runtime and if you want some good power and you have other attachments or you want to buy other attachments that are universal, an excellent buy. You will love the smoothness of it. You can easily pop a pin out here of that safety and the safety will be gone and it'll still be there, but the little flip part that's annoying will be gone and you will love using this trimmer. It's simply a great trimmer that probably could use a little bit more runtime or a little bit of uh I'd hate to say put a 12 amp hour or 15 amp hour battery on this and you'd get great runtime. You would. And the 12 amp hour battery isn't going to add much more weight, so why not? I think that would bump it up to the realm of where some of the other models are with lesser amp hour batteries.\nBut this unit really has a lot to offer the homeowner who really wants to have a lot of power and a lot of smoothness. I mean, this really reminds me of my steel when I'm out cutting with it is just butter smooth and really enjoyable to use. So after one year, I would still highly recommend this unit. Be careful with the head. Now the replacing that head's 30 bucks, but just be careful with it, don't beat on it and if something happens and it's not letting out line, take a look at it and just don't continue beating on it.\nThat's my take on this guy. Hope you guys enjoyed it. Please leave your comments below if you own this machine, if you have thoughts of buying it or anything else. It's always great to hear what other people have to say and a lot of people like to read that stuff and get your feedback also. We appreciate that. Give us a like in this video, subscribe to the channel if you haven't already. Thank you for your time. Have a great day.",
# #         "customer_sentiment_summary": {
# #             "positives": [
# #             "The product is highly praised for its power and performance.",
# #             "Users appreciate its reliability and durability.",
# #             "It receives positive feedback for being user-friendly and easy to operate.",
# #             "Customers mention the products efficiency and effectiveness in various tasks.",
# #             "The design and build quality are often highlighted as strong points.",
# #             "The product is considered good value for money by many users."
# #             ],
# #             "negatives": [
# #             "Some users report issues with battery life or charging time.",
# #             "A few customers mention the weight as a potential drawback for prolonged use.",
# #             "There are occasional complaints about noise levels during operation."
# #             ],
# #             "overall": "Overall, the sentiment is largely positive, with most users satisfied with the product's performance and features."
# #         }
# #     }
# # '''

# # content = Content(
# #     role="user",
# #     parts=[
# #         Part.from_uri("https://www.youtube.com/watch?v=Xt8Od-Z78Zs", mime_type="video/*"), # Important for video
# #         Part.from_text(prompt)
# #     ]
# # )

# # # Define the generation configuration
# # generate_content_config = types.GenerateContentConfig(
# #     temperature=1.0,
# #     top_p=0.8,
# #     max_output_tokens=2500,
# #     response_modalities=["TEXT"],
# #     safety_settings=[
# #         types.SafetySetting(
# #             category="HARM_CATEGORY_DANGEROUS_CONTENT",
# #             threshold="BLOCK_ONLY_HIGH"
# #         )
# #     ],
# # )

# # # Generate content and extract text
# # replies = []  # List to store extracted text
# # for chunk in client.models.generate_content_stream(
# #     model=model,
# #     contents=content,
# #     config=generate_content_config,
# # ):
# #     # Access the candidates attribute of the GenerateContentResponse object
# #     for candidate in chunk.candidates:
# #         content = candidate.content
# #         for part in content.parts:
# #             text = part.text
# #             if text:
# #                 replies.append(text)

# # # Join the replies into a single string
# # json_output = ''.join(replies)

# # # Remove unwanted characters
# # json_output = json_output.replace("json", "").replace("```", "")

# # # Ensure the JSON string is properly formatted
# # json_output = json_output.strip()

# # # Parse each JSON object
# # parsed_jsons = []

# # # print('json output: ' +json_output)

# # try:
# #     parsed_jsons.append(json.loads(json_output))

# #     full_transcript = parsed_jsons[0].get("transcript", "")
# #     summary = parsed_jsons[0].get("customer_sentiment_summary", {})

# #     df = pd.DataFrame({
# #         "transcript": [full_transcript],
# #         "transcript_summary": [summary],
# #         # "customer_sentiment": [sentiment]
# #     })

# #     print(df)

# #     st.write(df)

# # except json.JSONDecodeError as e:
# #     st.error(f"Error decoding JSON: {e}")
# #     st.error(f"Raw JSON output: {json_output}")




# ##################################################################################


# import streamlit as st
# import requests
# import json
# import pandas as pd
# from google.oauth2 import service_account
# import vertexai
# from vertexai.generative_models import GenerativeModel, Part, Content, GenerationConfig, HarmCategory, HarmBlockThreshold

# # Streamlit UI
# st.title("Video Sentiment Analysis")

# video_url = st.text_input("Enter YouTube Video URL:", "https://www.youtube.com/watch?v=Xt8Od-Z78Zs") # Default video
# if not video_url:
#     st.warning("Please enter a YouTube video URL.")
#     st.stop()


# # Vertex AI Configuration
# PROJECT_ID = "marine-actor-449411-t3"  # Replace with your project ID
# LOCATION = "us-central1"  # Replace with your region

# # Service Account Credentials
# credentials_path = 'C:\\Users\\pxs1101a\\Downloads\\Customer-Feedback-google-oauth\\Customer-Feedback-google-oauth\\SVCCredentials\\marine-actor-449411-t3-9022d9539783.json'

# try:
#     credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
#     vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials) # Use credentials here
#     st.success("Successfully authenticated with Vertex AI.")
# except Exception as e:
#     st.error(f"Error authenticating with Vertex AI: {e}")
#     st.stop() # Stop if authentication fails

# # Prompt
# prompt_text = """
#     Provide the full transcript without timeline and Customer Sentiment Summary without timeline in JSON format.
#     Ignore any Responsible AI violation part. You are an AI assistant that helps summarize this product's YouTube video transcription.
#     Provide the customer sentiment with all positives and all negatives based solely on the transcription.
#     If there are only negatives, provide only negative points, and if only positives are available, provide only positives.  Rank positives and negatives based on frequency.
#     The JSON should include "transcript" and "customer_sentiment_summary" fields. "customer_sentiment_summary" should have "positives", "negatives", and "overall" fields.
# """

# # Model Configuration
# model_name = "gemini-1.5-pro" # Or "gemini-1.5-pro-video" if you have access
# model = GenerativeModel(model_name)

# generation_config = GenerationConfig(
#     temperature=0.7,
#     top_p=0.9,
#     max_output_tokens=2048 #Adjust as needed.
# )

# safety_settings = {
#     HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
#     HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
# }

# # Analysis Function
# def analyze_video(video_url, prompt):
#     try:
#         content = Content(
#             role="user",
#             parts=[
#                 Part.from_uri(video_url, mime_type="video/*"),
#                 Part.from_text(prompt)
#             ]
#         )

#         responses = model.generate_content(
#             [content],
#             generation_config=generation_config,
#             safety_settings=safety_settings,
#             stream=False  #Important to set to false to get complete JSON
#         )

#         json_output = responses.text.strip() # get result.

#         try:
#             parsed_data = json.loads(json_output)

#             transcript = parsed_data.get("transcript", "Transcript not found.")
#             sentiment_summary = parsed_data.get("customer_sentiment_summary", {})
#             positives = sentiment_summary.get("positives", [])
#             negatives = sentiment_summary.get("negatives", [])
#             overall_sentiment = sentiment_summary.get("overall", "Overall sentiment not found.")

#             return transcript, positives, negatives, overall_sentiment

#         except json.JSONDecodeError as e:
#             st.error(f"JSON Decode Error: {e}")
#             st.error(f"Raw response: {json_output}") # debug
#             return None, None, None, None

#     except Exception as e:
#         st.error(f"An error occurred: {e}")
#         return None, None, None, None


# # Run Analysis
# if st.button("Analyze Video"):
#     with st.spinner("Analyzing video..."):
#         transcript, positives, negatives, overall_sentiment = analyze_video(video_url, prompt_text)

#         if transcript:
#             st.subheader("Transcript:")
#             st.write(transcript)

#             st.subheader("Sentiment Analysis:")

#             st.write("**Overall Sentiment:**", overall_sentiment)

#             if positives:
#                 st.write("**Positives:**")
#                 for positive in positives:
#                     st.write(f"- {positive}")

#             if negatives:
#                 st.write("**Negatives:**")
#                 for negative in negatives:
#                     st.write(f"- {negative}")
#         else:
#             st.warning("Analysis failed. Check the error messages above.")


#####################################################################################################################################################

import streamlit as st
import requests
import json
import pandas as pd
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel, Part, Content, GenerationConfig, HarmCategory, HarmBlockThreshold

# Streamlit UI
st.title("Video Sentiment Analysis")

video_url = st.text_input("Enter YouTube Video URL:", "gs://cloud-samples-data/video/animals.mp4") # Default video, CHANGE THIS TO YOUR GCS URL
if not video_url:
    st.warning("Please enter a YouTube or GCS video URL.")
    st.stop()


# Vertex AI Configuration
PROJECT_ID = "marine-actor-449411-t3"  # Replace with your project ID
LOCATION = "us-central1"  # Replace with your region

# Service Account Credentials
credentials_path = 'C:\\Users\\pxs1101a\\Downloads\\Customer-Feedback-google-oauth\\Customer-Feedback-google-oauth\\SVCCredentials\\marine-actor-449411-t3-9022d9539783.json'

try:
    credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=["https://www.googleapis.com/auth/cloud-platform"])
    vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials) # Use credentials here
    st.success("Successfully authenticated with Vertex AI.")
except Exception as e:
    st.error(f"Error authenticating with Vertex AI: {e}") # print error e
    st.stop() # Stop if authentication fails

# Prompt
prompt_text = """
    Provide the full transcript without timeline and Customer Sentiment Summary without timeline in JSON format.
    Ignore any Responsible AI violation part. You are an AI assistant that helps summarize this product's YouTube video transcription.
    Provide the customer sentiment with all positives and all negatives based solely on the transcription.
    If there are only negatives, provide only negative points, and if only positives are available, provide only positives.  Rank positives and negatives based on frequency.
    The JSON should include "transcript" and "customer_sentiment_summary" fields. "customer_sentiment_summary" should have "positives", "negatives", and "overall" fields.
    **Do not include any markdown formatting like ```json around the JSON output.**
"""

# Model Configuration
model_name = "gemini-1.5-pro" # Or "gemini-1.5-pro-video" if you have access
model = GenerativeModel(model_name)

generation_config = GenerationConfig(
    temperature=0.7,
    top_p=0.9,
    max_output_tokens=2048 #Adjust as needed.
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
            stream=False  #Important to set to false to get complete JSON
        )

        response_text = responses.text.strip()  # Get the raw text response

        # Remove ```json and ``` if present
        if response_text.startswith("```json"):
            response_text = response_text[6:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]


        try:
            parsed_data = json.loads(response_text)

            transcript = parsed_data.get("transcript", "Transcript not found.")
            sentiment_summary = parsed_data.get("customer_sentiment_summary", {})
            positives = sentiment_summary.get("positives", [])
            negatives = sentiment_summary.get("negatives", [])
            overall_sentiment = sentiment_summary.get("overall", "Overall sentiment not found.")

            return transcript, positives, negatives, overall_sentiment

        except json.JSONDecodeError as e:
            st.error(f"JSON Decode Error: {e}") # print error message
            st.error(f"Raw response: {response_text}")  # debug
            return None, None, None, None

    except Exception as e:
        st.error(f"An error occurred: {e}") # print error message
        return None, None, None, None


# Run Analysis
if st.button("Analyze Video"):
    with st.spinner("Analyzing video..."):
        transcript, positives, negatives, overall_sentiment = analyze_video(video_url, prompt_text)

        if transcript:
            st.subheader("Transcript:")
            st.write(transcript)

            st.subheader("Sentiment Analysis:")

            st.write("**Overall Sentiment:**", overall_sentiment)

            if positives:
                st.write("**Positives:**")
                for positive in positives:
                    st.write(f"- {positive}") #Show items

            if negatives:
                st.write("**Negatives:**")
                for negative in negatives:
                    st.write(f"- {negative}")  #Show items
        else:
            st.warning("Analysis failed. Check the error messages above.")