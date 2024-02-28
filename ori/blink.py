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
            bstick.set_color(red=255,green=0,blue=0)
            sleep(1)
            bstick.turn_off()