import random
from time import sleep
from blinkstick import blinkstick

NOTIFICATION_COLORS = {
    "unread Gmail messages":          (255, 0, 0),     # Red
    "today's Google Calendar events": (0, 255, 0),     # Green
    "today's Google Tasks":           (255, 165, 0),   # Orange
    "unread Outlook emails":          (0, 0, 255),     # Blue
    "today's calendar events":        (255, 255, 0),   # Yellow
    "unread Teams chat messages":     (255, 0, 255),   # Magenta
    "unread Teams channel messages":  (0, 255, 255),   # Cyan
}

def notify_alerts(alerts: dict):
    if len(blinkstick.find_all()) == 0:
        print("No BlinkStick devices found.")
        return
    
    # Notify the alerts
    print("Notifying alerts.")
    for bstick in blinkstick.find_all():
        print(f"Found BlinkStick: {bstick.get_serial()}")
        for alert_type, _ in alerts.items():
            print(alert_type)
            bstick.set_color(red=NOTIFICATION_COLORS[alert_type][0], green=NOTIFICATION_COLORS[alert_type][1], blue=NOTIFICATION_COLORS[alert_type][2])
            sleep(5)
            bstick.turn_off()


def startup_blinker():
    print("Starting Ori...")
    if len(blinkstick.find_all()) == 0:
        return
    
    # Test the blinker
    for bstick in blinkstick.find_all():
        for i in range(5):
            bstick.set_color(red=random.randint(0, 255), green=random.randint(0, 255), blue=random.randint(0, 255))
            sleep(0.5)
            bstick.turn_off()
            sleep(0.05)