#!/usr/bin/python3

import requests
def get_ip():
	url = "https://ipinfo.io/json"
	try:
		response = requests.get(url)
		if response.status_code == 200:
			ip_data = response.json()
			print("IP Address: ", ip_data.get("ip"))
			print("City: ", ip_data.get("city"))
			print("Region: ", ip_data.get("region"))
			print("Country: ", ip_data.get("country"))
			
			return ip_data.get("ip")
		else:
			return "******** failed to read the json... ********"
	except Exception as e:
		print(f'error occurred: {str(e)}\n')
