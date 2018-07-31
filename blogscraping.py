import requests 
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('http://www.ilfordrecorder.co.uk/home')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='teaser')

with open('post.csv', 'w') as csv_file:
  csv_writer = writer(csv_file)
  headers = ['Title', 'Link']
  csv_writer.writerow(headers)

  for post in posts:
    title = post.find(class_='teaser-title').get_text().replace('\n', '')
    link = post.find('a')['href']
    csv_writer.writerow([title, link])
