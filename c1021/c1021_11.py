import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# soup 변환
soup = BeautifulSoup(res.text,"lxml")
with open("c1021/melon.html","w",encoding="utf-8")as f:
    f.write(soup.prettify())

data = soup.find("div",{"class":"hot_issue"})
melons = data.find_all("ellipsis")
for idx,melon in enumerate(melons):
    title = melon.find("title").next.strip()
    print("제목 :",melon.find().next)
    print("가수 :",melon.find().next)
    print("출처 :",melon.find().next)
