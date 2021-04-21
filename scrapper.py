import pandas as pd
import requests
from bs4 import BeautifulSoup

# getting page url using request's get method
page = requests.get('https://forecast.weather.gov/MapClick.php?lat=33.9456&lon=-118.3922#.YH_BnegzZPY')

# now parsing requests object into html
soup = BeautifulSoup(page.content, 'html.parser')

# finding particular block u want to scrap
week = soup.find(id='seven-day-forecast-body')

items = week.find_all(class_='tombstone-container')
# print(items[0].find(class_='period-name').get_text())

period_name = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperatures = [item.find(class_='temp').get_text() for item in items]
# print(period_name)
# print(short_description)
# print(temperatures)

# this DataFrame() is converting ur list into a column formats and it take lists as a dictionary format
weather_stuff = pd.DataFrame({
    'Period': period_name,
    'Short Description': short_description,
    'Temperature': temperatures
})

print(weather_stuff)

# now converting into a csv file
# weather_stuff.to_csv('sample.csv')
