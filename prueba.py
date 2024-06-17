from bs4 import BeautifulSoup as bs
import lxml
import pymysql
import requests
import pandas as pd

url = "https://cuspide.com/100-mas-vendidos/"
response = requests.get(url)

libros = bs(response.content, "html.parser")
titulo = libros.find_all(class_="name product-title woocommerce-loop-product__title")

for i in titulo:
    print(i.get_text())



