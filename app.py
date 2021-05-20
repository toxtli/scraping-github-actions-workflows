import json
import requests
from datetime import datetime

url = 'https://httpbin.org/get'
response = requests.get(url)
data = response.json()
json.dump(data, open('data/dump-{}.csv'.format(datetime.today().strftime('%Y-%m-%d-%H-%M-%S')), 'w'))
