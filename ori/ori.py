import os
import asyncio
from dotenv import load_dotenv

from msgraph_python.api import *
from msgraph_python.exceptions import *


# Manage the Ori Application
class Ori:
    def __init__(self, api_client):
        self.api_client = api_client


def main():
    # Load the environment variables
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    tenant_id = os.getenv("TENANT_ID")
    if not check_env_vars(client_id, tenant_id):
        return
    asyncio.run(start_ori(client_id=client_id, tenant_id=tenant_id))


async def start_ori(client_id, tenant_id):
    # Create a new GraphAPI object, and validate the connection
    try: 
        api_client = await NewGraphAPI(client_id=client_id, tenant_id=tenant_id)
        ori = Ori(api_client=api_client)
    except AuthorizationException as e:
        print(f"{e}")
        return
    
    # Get the user info
    try:
        await ori.api_client.get_user_info()
    except RequestException as e:
        print(f"{e}")
        return


# Check if the environment variables are set
def check_env_vars(client_id, tenant_id):
    if not client_id:
        print("Please set the CLIENT_ID environment variable.")
        return False

    if not tenant_id:
        print("Please set the TENANT_ID environment variable.")
        return False

    return True


if __name__ == "__main__":
    main()