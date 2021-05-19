#!/usr/bin/python3.8

import urllib3
urllib3.disable_warnings()
import requests, bs4

res = requests.get('https://www.lavanguardia.com')
res.raise_for_status()
laVangSoup = bs4.BeautifulSoup(res.text, 'html.parser')
titularesRaw = laVangSoup.find_all("h2")
titulares = [el.text for el in titularesRaw]


links = []
for link in laVangSoup.find_all('h2'):
    links.append(link.find('a')['href'])

linksfull = ["https://www.lavanguardia.com" + elem for elem in links]

import xlsxwriter

workbook = xlsxwriter.Workbook(r'C:\Path\To\Location\FileName.xlsx')
worksheet = workbook.add_worksheet()

row = 1
row2 = 1
col = 0
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'HEADLINE', bold)
worksheet.write('B1', 'Link', bold)

for item in titulares:
    worksheet.write(row, col, item)
    row += 1
for elem in linksfull:
    worksheet.write(row2, col + 1, elem)
    row2 += 1

workbook.close()





