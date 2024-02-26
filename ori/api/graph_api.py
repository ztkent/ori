import time
import requests
from selenium import webdriver
from msal import PublicClientApplication

# This is an wrapper to interact with Teams and Outlook via the Microsoft Graph API
#
#

def NewGraphAPI(client_id, tenant_id, redirect_uri):
    # Create a "Public Client" to auth with the Graph API
    app_client = PublicClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
    )
    # Get the authorization request URL
    auth_url = app_client.get_authorization_request_url(
        ["https://graph.microsoft.com/.default"],
        redirect_uri=redirect_uri
    )

    # Vist the Auth URL and ask the user to login.
    browser = webdriver.Chrome()
    browser.get(auth_url)

    # Wait for the user to authorize the app and get redirected
    # TODO: InteractiveBrowserCredential
    # https://github.com/microsoftgraph/msgraph-sdk-python?tab=readme-ov-file#23-initialize-a-graphserviceclient-object
    
    start_time = time.time()
    while True:
        if "code=" in browser.current_url:
            break
        if time.time() - start_time > 120:
            raise Exception("Timeout reached while waiting for authorization code")
        time.sleep(1)
    # Extract the authorization code from the URL
    auth_code = browser.current_url.split("code=")[1].split("&")[0]
    # Close the browser
    browser.quit()

    # Acquire the token
    result = app_client.acquire_token_by_authorization_code(
        auth_code,
        ["https://graph.microsoft.com/.default"],
        redirect_uri=redirect_uri
    )

    if "access_token" in result:
        access_token = result['access_token']
    else:
        raise Exception("Failed to acquire access token")
    
    return GraphAPI(app_client, access_token, result['id_token_claims']['preferred_username'])


class GraphAPI:
    def __init__(self, client, access_token, username):
        self.client = client
        self.access_token = access_token
        self.username = username
    
    # Get the user account info
    # Requires the "User.Read" permission
    def get_user_info(self):
        # Call the Microsoft Graph API
        headers = {
            'Authorization': 'Bearer ' + self.access_token
        }
        response = requests.get(
            "https://graph.microsoft.com/v1.0/me",
            headers=headers
        )
        print(response.json())
       