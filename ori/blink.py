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
            strobe_light()

def strobe_light():
    # Check if there are any BlinkStick devices connected
    if len(blinkstick.find_all()) == 0:
        print("No BlinkStick devices found.")
        return

    # Strobe the light
    print("Strobing light.")
    for bstick in blinkstick.find_all():
        print(f"Found BlinkStick: {bstick.get_serial()}")
        for _ in range(5):
            color_hex = int(random.random()*0xFFFFFF)
            bstick.set_color(hex=color_hex)
            sleep(1)
            bstick.turn_off()
            sleep(0.5)