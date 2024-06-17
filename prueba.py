from bs4 import BeautifulSoup as bs
import lxml
import pymysql
import requests
import pandas as pd
import re 

url = "https://cuspide.com/100-mas-vendidos/"
url_dolar = "https://www.xe.com/es/currencyconverter/convert/?Amount=1&From=ARS&To=USD"
response_dolar = requests.get(url_dolar)
response = requests.get(url)

libros = bs(response.content, "html.parser")
titulo = libros.find_all(class_="name product-title woocommerce-loop-product__title")
precio = libros.find_all(class_="price")
url_libros = []
precio_libros = []
titulo_libros = []

url_error = []
titulo_error = []
datos_dolar = bs(response_dolar.content, "html.parser")
valor_dolar = datos_dolar.find(class_="sc-ac62c6d1-0 GwlFu")
precio_dolar = valor_dolar.get_text(strip= True)
limpieza_precio_dolar = precio_dolar.split(" ")
limpieza_precio_dolar = limpieza_precio_dolar[3]



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



dic = dict(Titulo = titulo_libros, Url = url_libros, Precio = precio_libros)
dic_errores = dict(Titulo = titulo_error, Url = url_error)
df_errores = pd.DataFrame(dic_errores)
df  = pd.DataFrame(dic)
print(limpieza_precio_dolar)
