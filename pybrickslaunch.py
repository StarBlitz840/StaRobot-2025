
import os
import subprocess
HUB_NAME = "Controller5"

target = os.getenv("TARGET")
command = f"pybricksdev run ble --name {HUB_NAME} {target}"

try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError:
    print("Error uploading code to hub")
    print("Make sure to set HUB_NAME and turn the hub on")