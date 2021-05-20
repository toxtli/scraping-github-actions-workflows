import json
import requests
from datetime import date

url = 'https://httpbin.org/get'
response = requests.get(request_url)
data = response.json()

json.dump(data, open('data/dump_{}.csv'.format(date.today().strftime('%Y%m%d'), 'w'))
          
