from camera import Camera
from backup import BackupUnit

import time

def main():
    cam = Camera()
    backup = BackupUnit(cam)

# Bro this cycle is just for reference  before a software integrate 
    for cycle in range(5):
        print(f"   Cycle {cycle+1}   ")
        cam.operate()
        backup.monitor()
        time.sleep(3)

    print("System  Monitoring Ended ")

if __name__ == "__main__":
    main()
