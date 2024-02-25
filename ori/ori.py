import os
from .api.graph_api import *
from dotenv import load_dotenv


def main():
    # Load the environment variables
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    tenant_id = os.getenv("TENANT_ID")
    user_principal_name = os.getenv("USER_PRINCIPAL_NAME")
    if not check_env_vars(client_id, client_secret, tenant_id, user_principal_name):
        return

    # Create a new GraphAPI object
    ori = NewGraphAPI(client_id, client_secret, tenant_id, user_principal_name)
    ori.get_user_info()


# Check if the environment variables are set
def check_env_vars(client_id, client_secret, tenant_id, user_principal_name):
    if not client_id:
        print("Please set the CLIENT_ID environment variable.")
        return False

    if not client_secret:
        print("Please set the CLIENT_SECRET environment variable.")
        return False

    if not tenant_id:
        print("Please set the TENANT_ID environment variable.")
        return False

    if not user_principal_name:
        print("Please set the USER_PRINCIPAL_NAME environment variable.")
        return False

    return True

if __name__ == "__main__":
    main()