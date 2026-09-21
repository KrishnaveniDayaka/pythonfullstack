
import pandas as pd
import requests
from bs4 import BeautifulSoup
URL = "https://timely-sunshine-e821b3.netlify.app/"
page = requests.get(URL)
print("Status Code:", page.status_code)
htmlCode = page.text
soup = BeautifulSoup(htmlCode, "html.parser")
items = soup.find_all("div", class_="a")
names = []
prices = []
images = []
for item in items:
    name_tag = item.find("div", class_="name")
    price_tag = item.find("div", class_="price")
    image_tag = item.find("div", class_="image").find("img")
    name = name_tag.text.strip() if name_tag else None
    price = price_tag.text.strip() if price_tag else None
    image_src = image_tag["src"] if image_tag else None
    names.append(name)
    prices.append(price)
    images.append(image_src)
df = pd.DataFrame({
    "Product_Name": names,
    "MRP": prices,
    "Image_SRC": images
})
print("\nScraped Data:")
print(df)
csv_filename = "productdetails.csv"
df.to_csv(csv_filename, index=False)
print(f"\nCSV file saved as: {csv_filename}")