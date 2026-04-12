import requests
import sys
import hashlib

# Arguments passed from HA
username = sys.argv[1]
password = sys.argv[2]
device_code = sys.argv[3]
protocolCode = sys.argv[4]
temperature = sys.argv[5]

login_url = 'https://cloud.linked-go.com:449/crmservice/api/app/user/login'
control_url = 'https://cloud.linked-go.com:449/crmservice/api/app/device/control'

try:
    # 1. Get Token
    password_md5 = hashlib.md5(password.encode("utf-8")).hexdigest()
    login_data = {"userName": username, "password": password_md5}
    r = requests.post(login_url, json=login_data, timeout=10)
    token = r.json()['objectResult']['x-token']

    # 2. Set Temperature
    headers = {"x-token": token, "Content-Type": "application/json; charset=utf-8"}
    payload = {
        "param": [
            {"deviceCode": device_code, "protocolCode": protocolCode, "value": temperature},
            {"deviceCode": device_code, "protocolCode": "22", "value": temperature}
        ]
    }
    
    response = requests.post(control_url, headers=headers, json=payload, timeout=10)
    print(f"Success: {response.json().get('error_msg')}")

except Exception as e:
    print(f"Error: {str(e)}")
    sys.exit(1)