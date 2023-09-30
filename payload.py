import time
import requests
import math
import random
from datetime import datetime

TOKEN = "BBFF-dxn8Kle7W8WnJdQNGJmoDqu4zPrudO"  # Put your TOKEN here
DEVICE_LABEL = "sic-4-aliya"  # Put your device label here 
VARIABLE_LABEL_1 = "data_parkir"  # Put your first variable label here
VARIABLE_LABEL_2 = "name"  # Put your second variable label here
VARIABLE_LABEL_3 = "kelas"  # Put your second variable label here

now = datetime.now()

def send_ubidots(value1, value2, value3):
    payload = build_payload(
        VARIABLE_LABEL_1, VARIABLE_LABEL_2, VARIABLE_LABEL_3, value1, value2, value3)

    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")
    
def build_payload(variable_1, variable_2, variable_3, value1, value2, value3):
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    payload = {variable_1: {"value": 1, "context": {"waktu": dt_string, "id_card": value1, "name": value2, "kelas":value3}}}

    return payload
    
def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(1)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, your device is updated")
    return True

