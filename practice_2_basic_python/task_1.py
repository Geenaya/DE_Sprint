import requests as req
from bs4 import BeautifulSoup
import json

data = {
    "data":[]
}

for page in range(1, 3):
    url = "https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post"
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa": "serp-item__title"})

    for iter in tags:
        url_obj = iter.attrs["href"]
        resp_obj = req.get(url_obj)
        soup_obj = BeautifulSoup(resp.text, "lxml")
        tag_exp = soup.find(attrs={"class":"vacancy-description-list-item"}).find(attrs={"data-qa":"vacancy-experience"}).text
        tag_salary = soup.find(attrs={"data-qa":"vacancy-salary"}).find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}).text
        tag_region = soup.find(attrs={"data-qa":"vacancy-address-with-map"}).find(attrs={"data-qa":"vacancy-view-raw-address"}).text

        print(iter.text)
        data["data"].append({"title": iter.text, "work experience": tag_exp, "salary": tag_salary, "region": tag_region})

        with open("data.json", "w") as file:
            json.dump(data,file, ensure_ascii=False)
