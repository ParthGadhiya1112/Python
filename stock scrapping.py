import  pandas as pd
import requests
from bs4 import BeautifulSoup

# if u want to check than copy below link and browse it
page = requests.get('https://economictimes.indiatimes.com/indices/sensex_30_companies?sortby=companyname&sortorder=asc')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)

shares = soup.find(class_='data_display')
company = shares.find_all(class_='dataList')
company_name = [name.find('a').get_text() for name in company]
current_price = [price.find(class_='ltp').get_text() for price in company]
current_change = [change.find(class_='change').get_text() for change in company]
# print(company_name)
# print(current_price)
# print(current_change)

# making table using pandas library
live_stock = pd.DataFrame({
    'Company Name': company_name,
    'Current Price': current_price,
    'Change(Rs)': current_change
})

print(live_stock)