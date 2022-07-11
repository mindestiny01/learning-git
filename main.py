import requests
from bs4 import BeautifulSoup
import pandas as pd



url = https://www.facebook.com
header = {'user-info' : ''}

first_req = requests.get(url, headers = header)
first_soup = BeautifulSoup(first_req.content, 'html.parser')

print(first_req.status_code)
print(first_soup.prettify())
