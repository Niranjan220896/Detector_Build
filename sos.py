import time

def trigger_sos():
    print("SOS Sending Emergency Signal..")
    for _ in range(5,26):
        print("SOS::  Vibrating Beeping..  Flashing Light.")
        time.sleep(5)
    print("SOS SOS Completed.\n")
