import requests

URL = "https://o3m5qixdng.execute-api.us-east-1.amazonaws.com/api/managers"

def fetch_supervisors():
	"""
	Fetch a list of supervisors from a client-specified URL.
	"""
	response = requests.get(URL)
	return list(response.json())