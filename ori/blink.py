import random
from time import sleep
from blinkstick import blinkstick

def notify_alerts(alerts: dict):
    # Check if there are any BlinkStick devices connected
    if len(blinkstick.find_all()) == 0:
        print("No BlinkStick devices found.")
        return

    # Notify the alerts
    print("Notifying alerts.")
    for bstick in blinkstick.find_all():
        print(f"Found BlinkStick: {bstick.get_serial()}")
        for alert_type, _ in alerts.items():
            print(alert_type)
            bstick.set_color(name=alert_type, red=255, green=0, blue=0)
            sleep(1)

def startup_blinker():
    print("Starting Ori...")

    # Check if there are any BlinkStick devices connected
    if len(blinkstick.find_all()) == 0:
        return

    # Notify the alerts
    for bstick in blinkstick.find_all():
        for i in range(5):
            bstick.set_color(red=random.randint(0, 255), green=random.randint(0, 255), blue=random.randint(0, 255))
            sleep(0.5)
            bstick.turn_off()
            sleep(0.05)