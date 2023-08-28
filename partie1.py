import advertools as adv
#imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import os
import wget
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
import xlrd
import requests
from urllib.request import urlopen
import urllib
import openpyxl
import numpy as np
import csv
import openpyxl
import pandas.io.sql as psql
from pandas import read_csv
from argparse import ArgumentParser, FileType
from multiprocessing.pool import ThreadPool
import re
from urllib import request
import shutil
import pyodbc
import sqlalchemy
import gzip
import xml.etree.ElementTree as ET

headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en,mr;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}

        list_column = ["url"]


# Créer le dictionnnaire qui va posséder toute nos valeurs avec comme clé l'élement css
def create_data(list_column,list_res):
    data = {}
    compt_key = 0
    compt_value = 0
    while(compt_key<len(list_column)):
        e = [list_column[compt_key]]
        strs = ' '.join(e)
        data[strs] = list_res[compt_value]
        compt_value += 1
        compt_key += 1
    return data


s=Service('C:votre_chemin/chromedriver.exe')
driver = webdriver.Chrome(service=s)
#open the webpage
list_url = []
driver.get("http://tripadvisor-sitemaps.s3-website-us-east-1.amazonaws.com/2/fr/sitemap_fr_index.xml")
req = requests.get("http://tripadvisor-sitemaps.s3-website-us-east-1.amazonaws.com/2/fr/sitemap_fr_index.xml",headers=headers,timeout=5,verify=True)
soup = BeautifulSoup(req.text, features="xml")
soup.prettify()
print (req.status_code)
for i in range(1,372):
    container = driver.find_elements(By.XPATH,f"//*[@id='folder{i}']")
    for j in container:
        x = driver.find_element(By.TAG_NAME, 'loc').text
        soup = BeautifulSoup(j.text, 'html.parser')
        soup.prettify()
        try:
            noms_resto = soup.find("loc")
            if "restaurant" in noms_resto.get_text(strip=True):
                list_url.append(noms_resto.get_text(strip=True))
            else:
                pass
        except:
            pass
print(list_url)



print(len(list_url))
list_urls = []
list_urlss = []
compteur_max = len(list_url)+1
ok = []
pd.set_option("display.max_rows",10000000)
pd.set_option("display.max_columns",10000000)
for element in list_url:
    nyt_news = adv.sitemap_to_df(element)
    df = pd.DataFrame(nyt_news)
    for e in df["loc"]:
        list_urls.append(e) 
population_dict = create_data(list_column,list_urls)


liste = []
for i in list_urls:
    if "Brussels" in (" " + i + " "):
        liste.append(i)
    else:
        pass
print(liste)


#telecharge données sur excel et crée le fichier
# dictionnaire avec les données à intégrer au fichier excel
def data_excel(data,nom_fichier):
    path = 'C:votre_chemin/python/'
    os.chdir(path)
    wb_sortie = openpyxl.Workbook()#fichier de sortie
    sheet = wb_sortie.active
    row = 2
    s = 0
    y = 18000
    x = 0
    
    return wb_sortie.save(nom_fichier+".xlsx")
data_excel(mon_dictionnaire,"tsg")

dict_url = {"url":liste}


pd.DataFrame(dict_url)

df = pd.DataFrame(dict_url)

print(df)
df.to_excel(r'C:/votre_chemin/python/urls_brussels_tripadvisor.xlsx', index=False)