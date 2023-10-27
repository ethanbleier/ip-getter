#!/usr/bin/python3
import requests

def get_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            ip = response.json()["ip"]
            print('fetched', ip)
            return ip
        else:
            print(f"Failed to retrieve IP. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None

# Example usage:
if __name__ == "__main__":
    ip_address = get_ip()
    if ip_address:
        print(f"Your public IP address is: {ip_address}")
    else:
        print("Failed to retrieve the IP address.")
