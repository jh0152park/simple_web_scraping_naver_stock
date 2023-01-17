import csv
import requests
from bs4 import BeautifulSoup

filename = "코스피 시가총액.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
writer.writerow("N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split())

for page in range(1, 5):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page={}".format(page)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    trs = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) <= 1:
            continue
        datas = [td.get_text().strip() for td in tds][:-1]
        writer.writerow(datas)

