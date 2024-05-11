import requests
from bs4 import BeautifulSoup as soup
import csv

source = requests.get('https://www.layers.shop/collections/realme-gt-master-edition')

webpage = soup(source.content, features="html.parser")

# print out html
# print((webpage.prettify()))

name = []

price = []


for i in webpage.find_all(class_='cta-container_title'):
    string = i.span.text
    name.append(string.strip())

for i in webpage.find_all(class_='price'):
    string = i.span.text
    substring = string.rpartition('₹')[2]
    price.append(substring.strip())

    
    
file_name = 'scrape.csv'

with open(file_name, "w", encoding="utf-8") as f:
    f.write = csv.writer(f)
    f.write.writerow(['No.', 'Name', 'Price'])
    
    for i in range(len(price)):
        f.write.writerow([i+1, name[i], price[i]])