from bs4 import BeautifulSoup
import requests

URL = 'https://www.google.com'
response = requests.get(URL)
soup = BeautifulSoup(response.content)

print(soup.title)
print(soup.find('h1'))
print(soup.text)
