import requests

api_url = 'https://api.open-notify.org/iss-now.json'

response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)