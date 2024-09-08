import json
import requests
import time

x1 = 4454509
y1 = 3434918
x2 = 4457210
# x2 = 4454529
y2 = 3429017

url = 'https://api.open-elevation.com/api/v1/lookup'

data = []

outcome = []

for x in range(x1, x2):
    chunk = { 'locations': []}
    for y in range(y1, y2, -1):
        obj = {
            "latitude": x / 100000,
			"longitude": y / 100000
        }
        chunk["locations"].append(obj)
        print(obj)

    def fetchData():
        try:
            results = requests.post(url, json = chunk).json()['results']
            results = list(map((lambda obj: obj['elevation']), results))
            outcome.append(results)
        except:
            time.sleep(10000)
            fetchData()
    fetchData()

with open('data.json', 'w+') as f:
    json.dump(outcome, f)

print('>>> FINISHED')