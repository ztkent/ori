from msgraph_python.exceptions import *
from googleapi_python.exceptions import *

# Manage the Ori Application
class Ori:
    def __init__(self, graph_api=None, google_api=None):
        self.graph_api = graph_api
        self.google_api = google_api

    async def get_alerts(self, selected_services=[], selected_scopes=[]):
        alert_results = {}
        selected_channels = {}
        # Get the alerts from the selected Google channels
        if "google" in selected_services:
            google_channels = {}
            if "mail" in selected_scopes:
                temp_channels = {
                    # "get Gmail messages": ("Google Gmail", self.google_api.get_gmail_messages),
                    "unread Gmail messages": ("Google Gmail", self.google_api.get_unread_gmail_messages),
                }
                google_channels.update(temp_channels)
            if "calendar" in selected_scopes:
                temp_channels = {
                    # "get Google Calendar events": ("Google Calendar", self.google_api.get_calendar_events),
                    "today's Google Calendar events": ("Google Calendar", self.google_api.get_todays_calendar_events),
                }
                google_channels.update(temp_channels)
            # Add all Google Channels in scope to the selected channels
            selected_channels.update(google_channels)

        # Get the alerts from the selected Microsoft channels
        if "microsoft" in selected_services:
            microsoft_channels = {}
            if "mail" in selected_scopes:
                temp_channels = {
                    # "get Outlook emails": ("Microsoft Outlook", self.graph_api.get_outlook_emails),
                    "unread Outlook emails": ("Microsoft Outlook", self.graph_api.get_unread_outlook_emails),
                }
                microsoft_channels.update(temp_channels)
            if "calendar" in selected_scopes:
                temp_channels = {
                    # "get calendar events": ("Microsoft calendar", self.graph_api.get_all_calendar_events),
                    "today's calendar events": ("Microsoft Calendar", self.graph_api.get_todays_calendar_events),
                }
                microsoft_channels.update(temp_channels)
            if "teams-chat" in selected_scopes:
                temp_channels = {
                    # "get Teams chat messages": ("Microsoft Teams Chat", self.graph_api.get_all_teams_chats),
                    "unread Teams chat messages": ("Microsoft Teams Chat", self.graph_api.get_all_unread_teams_chat_messages),
                }
                microsoft_channels.update(temp_channels)
            if "teams-channel" in selected_scopes:
                temp_channels = {
                    # "get Teams channel messages": ("Microsoft Teams Channels", self.graph_api.get_teams_channel_messages),
                    "unread Teams channel messages": ("Microsoft Teams Channels", self.graph_api.get_unread_teams_channel_messages),
                }
                microsoft_channels.update(temp_channels)
            # Add all Microsoft Channels in scope to the selected channels
            selected_channels.update(microsoft_channels)
        
        # Get the alerts from each channel
        for alert_type, (channel_name, channel_func) in selected_channels.items():
            try:
                # Microsoft API calls are async, so we need to await them
                if "Microsoft" in channel_name:
                    alerts = await channel_func()
                # Other API calls are not async, so we can call them directly
                else:
                    alerts = channel_func()
                if alerts:
                    alert_results[alert_type] = alerts
            except Exception as e:
                print(f"An error occurred while getting {alert_type} from {channel_name}: {e}")

        return alert_results