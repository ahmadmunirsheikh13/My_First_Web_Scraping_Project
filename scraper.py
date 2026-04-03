import requests
from bs4 import BeautifulSoup
base_url="https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={}"
with open("products.csv","w",newline="") as file:
    file.write("Title,Price,Description,Rating\n")
    for page in range(1, 21):
        url=base_url.format(page)
        r=requests.get(url)
        soup=BeautifulSoup(r.text,"html.parser")
        products=soup.find_all("div",class_= "card thumbnail")
        for product in products:
            title=product.find("a",class_="title").text.strip()
            price=product.find("h4",class_="price").text.strip()
            description=product.find("p",class_="description").text.strip()
            rating=product.find("div",class_="ratings").text.strip()
            if title and price and description and rating:
                file.write(f"{title},{price},{description},{rating}\n")
            
     