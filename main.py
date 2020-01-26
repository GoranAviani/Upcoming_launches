import requests

request = requests.get('https://launchlibrary.net/1.3/launch')
print(request)
print(request.status_code)

for x in request.json()["launches"]:
    print("---------------")
    print(x)
    moreInfoURL = "https://launchlibrary.net/1.3/launch/" + str(x['id'])
    moreInfo = requests.get(moreInfoURL)
    print(moreInfo.json())
    print(moreInfo.status_code)

