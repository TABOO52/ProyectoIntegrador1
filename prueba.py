from bs4 import BeautifulSoup as bs
import lxml
import pymysql
import requests
import pandas as pd

url = "https://cuspide.com/100-mas-vendidos/"
response = requests.get(url)
print(response.text)

