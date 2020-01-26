import requests

request = requests.get('https://launchlibrary.net/1.3/launch')
print(request)
print(request.status_code)

for x in request.json()["launches"]:
    print("---------------")
    print(x)


