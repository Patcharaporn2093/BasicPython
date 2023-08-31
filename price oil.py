# oil.py

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def writetocsv(data):

	date = datetime.now().strftime('%Y-%m-%d')

	with open('data-price-oil-{}.csv'.format(date),'a',newline='',encoding='utf-8') as file:
		filewriter = csv.writer(file)
		filewriter.writerow(data)


url = 'https://www.shell.co.th/th_th/motorists/shell-fuels/fuel-price/app-fuel-prices.html#'

webopen = urlopen(url) # เปิดเว็บโดยไม่ต้องเปิด google chrome
html_page = webopen.read() #อ่านข้อมูลในเว็บ
webopen.close() # ปิดเว็บ

data = BeautifulSoup(html_page,'html.parser') #แปลงโค้ดให้ bs4 ช่วยแปล

title = data.find_all('td',{'data-h-title':'ผลิตภัณฑ์'})
price = data.find_all('td',{'data-h-title':'บาท/ลิตร'})

all_oil = []
for i in title:
	all_oil += [i.text]

all_price = []
for j in price:
	all_price += [j.text]

for i in range(9):
	all_data = (all_oil[i],all_price[i])
	writetocsv(all_data)
	
print('saved')