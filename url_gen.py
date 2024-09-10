import json
import requests
import time

x1 = 445450
y1 = 343491
x2 = 445721
# x2 = 4454529
y2 = 342901

url = 'https://api.open-elevation.com/api/v1/lookup'

data = []

outcome = []

for x in range(x1, x2):
    chunk = { 'locations': []}
    for y in range(y1, y2, -1):
        obj = {
            "latitude": x / 10000,
			"longitude": y / 10000
        }
        chunk["locations"].append(obj)

    def fetchData():
        try:
            with open('data.json', 'a') as f:
                results = requests.post(url, json = chunk).json()['results']
                results = list(map((lambda obj: obj['elevation']), results))
                f.write(str(results) + "\n")
            print(">>> LAP APPENDED")
        except:
            print(">>> REQUEST FAILED, RETRYING")
            time.sleep(1)
            fetchData()
    fetchData()

print('>>> FINISHED')