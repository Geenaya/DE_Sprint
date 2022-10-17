import requests as req
from bs4 import BeautifulSoup
import json
#import tqdm

data = {
    "data":[]
}
url = "https://vuejs.org/guide/introduction.html"
resp = req.get(url)
#print(resp.text)
soup = BeautifulSoup(resp.text, "lxml")
tags = soup.find_all("h2")

for iter in tags:
    print(iter.text)
    data["data"].append({"Title":iter.text})

    with open("data.json","w") as file:
        json.dump(data,file, ensure_ascii=False)
