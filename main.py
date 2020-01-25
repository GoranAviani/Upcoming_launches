import requests

request = requests.get('https://launchlibrary.net/1.3/launch')
print(request.text)
print(request.status_code)


