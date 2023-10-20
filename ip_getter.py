#!/usr/bin/python3

import requests
import os

def get_ip():
    url = "https://ipinfo.io/json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            ip_data = response.json()
            file_path = "tmp/ip.txt"

            # Check if the file already exists
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write(ip_data.get("ip"))
            else:
                print("File already exists. Not overwriting.")

            return f'IP address ({ip_data.get("ip")}) has been saved to {file_path}.'
        else:
            return "******** failed to read the JSON... ********"
    except Exception as e:
        return f'Error occurred: {str(e)}'

if __name__ == '__main__':
    result = get_ip()
    print(result)
