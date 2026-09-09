
import requests
url="https://lbrce.ac.in/"
response=requests.get(url)
print(response)
print(response.elapsed)