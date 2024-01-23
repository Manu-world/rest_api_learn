import requests

endpoint = "http://localhost:8000/api"

# Use the json parameter instead of params for sending JSON data
get_response = requests.get(endpoint, json={"query": "hello query"})
print(get_response.json())
