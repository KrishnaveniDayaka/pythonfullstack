
import requests
from bs4 import BeautifulSoup
url="https://lbrce.ac.in/"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
print(soup.find_all("a"))