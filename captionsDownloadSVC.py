from google.oauth2 import service_account
import googleapiclient.discovery

def main():
    # Path to the service account key file
    service_account_file = 'genai-sandbox-399108-97b35a701c02.json'

    # Define the required scopes
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Create credentials using the service account
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes)

    # Build the YouTube API client
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # Make a request to the YouTube API to list captions
    list_request = youtube.captions().list(
        part="snippet",
        videoId="M7FIvfx5J10"
    )
    list_response = list_request.execute()

    # Find the caption track ID for the desired language
    caption_id = None
    for item in list_response.get("items", []):
        if item["snippet"]["language"] == "en":  # Change "en" to the desired language code
            caption_id = item["id"]
            break

    if caption_id is None:
        print("No captions found for the specified language.")
        return

    # Make a request to download the caption track
    download_request = youtube.captions().download(
        id=caption_id,
        tfmt="srt"  # You can also use "vtt" for WebVTT format
    )

    # Execute the request and capture the response
    response = download_request.execute()

    # Print the captions
    captions = response.decode("utf-8")
    print(captions)

if __name__ == "__main__":
    main()