import requests
from bs4 import BeautifulSoup
import pandas as pd 

all_books=[]

base_url="https://books.toscrape.com/catalogue/page-{}.html"

for page in range(1,51):
    print(f"scrapes page {page}")
    url=base_url.format(page)
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    books=soup.find_all("article",class_="product_pod")
    
    for book in books:
        title=book.h3.a["title"]
        price=book.find("p",class_="price_color").text
        rating=book.p["class"][1]
        all_books.append({
            "Title":title,
            "Price":price,
            "Rating":rating
        })

df=pd.DataFrame(all_books)
df.to_csv("all_books.csv",index=False)
print("All Data Saved to CSV")