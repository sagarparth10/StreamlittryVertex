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

    # Make a request to the YouTube API
    request = youtube.captions().list(
        part="snippet",
        videoId="M7FIvfx5J10"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()