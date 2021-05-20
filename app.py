import json
import requests
from datetime import date

url = 'https://httpbin.org/get'
response = requests.get(url)
data = response.json()
json.dump(data, open('data/dump-{}.csv'.format(date.today().strftime('%Y-%m-%d-%H-%M-%S')), 'w'))
