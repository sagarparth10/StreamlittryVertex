import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(host='127.0.0.1', port=5000)

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