import requests
from msal import ConfidentialClientApplication

# This is an wrapper to interact with Teams and Outlook via the Microsoft Graph API
#
#

def NewGraphAPI(client_id,client_secret,tenant_id, user_principal_name):
    # Create a "App Client" to auth with the Graph API
    app_client = ConfidentialClientApplication(
        client_id,
        authority=f"https://login.microsoftonline.com/{tenant_id}",
        client_credential=client_secret,
    )
    return GraphAPI(app_client, user_principal_name)


class GraphAPI:
    def __init__(self, client, user_principal_name):
        self.client = client
        self.user_principal_name = user_principal_name
    
    # Get the user account info
    # Requires the "User.Read.All" permission
    def get_user_info(self):
        # Get the access token
        result = self.client.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])
        if "access_token" in result:
            # Call the Microsoft Graph API
            headers = {
                'Authorization': 'Bearer ' + result['access_token']
            }
            response = requests.get(
                f"https://graph.microsoft.com/v1.0/users/{self.user_principal_name}",
                headers=headers
            )
            print(response.json())
        else:
            print(f"Error: {result.get('error')}\nDescription: {result.get('error_description')}\nCorrelation ID: {result.get('correlation_id')}")

