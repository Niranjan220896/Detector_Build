import random

class Camera:
    def __init__(self):
        self.status = "Active"

    def operate(self):
        fault = random.choice([True, False, False])  # 33% chance to fail
        if fault:
            self.status = "Inactive"
            print("Camera ERROR: Camera Failure Detected!")
        else:
            self.status = "Active"
            print(" Camera is Working Normally.")
