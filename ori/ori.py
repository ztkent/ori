import os
import asyncio
import argparse
from time import sleep
from dotenv import load_dotenv
from blinkstick import blinkstick

import ori.blink as ori_blink
from ori.ori_class import Ori
from msgraph_python.api import *
from googleapi_python.api import *

def main():
    # Load the environment variables
    load_dotenv()

    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Start Ori")
    parser.add_argument('-service', type=str, default="google,microsoft" ,help='Select services to enable. Example: -service "google,microsoft"')
    parser.add_argument('-scopes', type=str, default="mail,calendar,teams-chat,teams-channel" ,help='Select notification channels to enable. Example: -scopes "mail,calendar,teams-chat,teams-channel"')
    args = parser.parse_args()
    
    # Select the services to enable
    selected_services = args.service.split(",")
    print(f"Selected services: {selected_services}")
    if len(selected_services) == 0:
        print("No services selected.")
        return

    # Select the scopes to enable
    selected_scopes = args.scopes.split(",")
    print(f"Selected scopes: {selected_scopes}")
    if len(selected_scopes) == 0:
        print("No scopes selected.")
        return

    # Start the Ori application
    asyncio.run(start_ori(selected_services, selected_scopes))

async def start_ori(selected_services, selected_scopes):
    ori = Ori()
    ori_blink.startup_blinker()
    # Create a new GoogleAPI client
    if "google" in selected_services:
        try: 
            google_api = NewGoogleAPI(scopes=selected_scopes)
            ori.google_api = google_api
        except GoogleAuthorizationException as e:
            print(f"{e}")
            return
    
    # Create a new GraphAPI client
    if "microsoft" in selected_services:
        try: 
            graph_api = await NewGraphAPI(scopes=selected_scopes)
            ori.graph_api = graph_api
        except MicrosoftAuthorizationException as e:
            print(f"{e}")
            return

    # Start checking every few minutes for new alerts
    while True:    
        try:
            alerts = await ori.get_alerts(selected_services, selected_scopes)
            if alerts:
                print(f"New alerts: {len(alerts)}")
                ori_blink.notify_alerts(alerts=alerts)
            else:
                print("No new alerts.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait 3 minutes before checking again
        await asyncio.sleep(180)