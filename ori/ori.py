import os
from .api.graph_api import *
from dotenv import load_dotenv


class Ori:
    def __init__(self, api):
        self.api = api # GraphAPI object

def main():
    # Load the environment variables
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    tenant_id = os.getenv("TENANT_ID")
    redirect_uri = os.getenv("REDIRECT_URI")
    if not check_env_vars(client_id, tenant_id, redirect_uri="https://login.microsoftonline.com/common/oauth2/nativeclient"):
        return

    # Create a new GraphAPI object
    try: 
        ori = Ori(NewGraphAPI(client_id, tenant_id, redirect_uri))
    except Exception as e:
        print(f"Failed to Create new : {e}")
        return
    
    ori.api.get_user_info()


# Check if the environment variables are set
def check_env_vars(client_id, tenant_id, redirect_uri):
    if not client_id:
        print("Please set the CLIENT_ID environment variable.")
        return False

    if not tenant_id:
        print("Please set the TENANT_ID environment variable.")
        return False
    if not redirect_uri:
        print("Please set the REDIRECT_URI environment variable.")
        return False

    return True

if __name__ == "__main__":
    main()