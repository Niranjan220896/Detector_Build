# backup.py

from sos import trigger_sos
import time

class BackupUnit:
    def __init__(self, camera):
        self.camera = camera

    def monitor(self):
        print("[BackupUnit] Monitoring Camera...")
        if self.camera.status == "Inactive":
            self.handle_failure()
        else:
            print("[BackupUnit] Camera OK.\n")

    def handle_failure(self):
        print("[BackupUnit] Camera Failure! Taking Backup Actions.")
        self.capture_images()
        trigger_sos()

    def capture_images(self):
        print("[BackupUnit] Capturing Images...")
        for i in range(3):
            print(f"        Image {i+1} captured.")
            time.sleep(5)
