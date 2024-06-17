from bs4 import BeautifulSoup as bs
import lxml
import pymysql
import requests
import pandas as pd

url = "https://cuspide.com/100-mas-vendidos/"
response = requests.get(url)

libros = bs(response.content, "html.parser")
titulo = libros.find_all(class_="name product-title woocommerce-loop-product__title")
precio = libros.find_all(class_="price")
url_libros = []
precio_libros = []
titulo_libros = []

url_error = []
titulo_error = []

for i , j in zip(precio,titulo):
    try:
        titulo_ = j.find("a").get_text()
        url_ = j.find("a").get("href")
        precio_ = i.find("bdi").get_text(strip = True).replace("$","").replace(".","").replace(",",".")  
        
        titulo_libros.append(titulo_)
        url_libros.append(url_)
        precio_libros.append(float(precio_))
    except AttributeError:
        url_error.append(url_)
        titulo_error.append(titulo_)

print(precio_libros)
print(url_libros)
print(url_error)
print(titulo_libros)
