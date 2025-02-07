from flask import Flask, redirect, url_for, session, request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

# OAuth 2.0 Client ID and Client Secret
CLIENT_ID = '542074524698-nd9oh93fi05epsodoh1fr17l9ennc85n.apps.googleusercontent.com'
CLIENT_SECRET = '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'

# OAuth 2.0 configuration
# SCOPES = ['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email']
SCOPES = [
    'openid',
    'https://www.googleapis.com/auth/userinfo.profile',
    'https://www.googleapis.com/auth/userinfo.email'
]

REDIRECT_URI = 'https://127.0.0.1:5000/callback'

# Path to the client secrets file
CLIENT_SECRETS_FILE = 'client_secrets.json'

@app.route('/')
def index():
    return 'Welcome to the Google OAuth 2.0 example! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    # Create the flow using the client secrets file
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )

    # Generate the authorization URL
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )

    # Store the state in the session
    session['state'] = state

    # Redirect the user to the authorization URL
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    # Retrieve the state from the session
    state = session['state']

    # Create the flow using the client secrets file
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri=REDIRECT_URI
    )

    # Fetch the authorization response URL
    authorization_response = request.url

    # Exchange the authorization code for credentials
    flow.fetch_token(authorization_response=authorization_response)

    # Store the credentials in the session
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return 'Login successful! <a href="/profile">View Profile</a>'

@app.route('/profile')
def profile():
    # Load the credentials from the session
    credentials = Credentials(**session['credentials'])

    # Check if the credentials are valid
    if not credentials.valid:
        if credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            return redirect(url_for('login'))

    # Use the credentials to access the Google API
    # For example, you can use the Google People API to get the user's profile information

    return 'User profile information goes here.'


@app.route('/youtube')
def youtube():
    



def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

if __name__ == '__main__':
    # Run the Flask application
    app.run(ssl_context='adhoc', host='127.0.0.1', port=5000)