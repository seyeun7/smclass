import requests
# res = requests.get("http://www.google.com")


# User-Agent 크롬브라우저 정보로 변경해서 전달
url = "http://www.melon.com"
headers = {"User-Agent":"Moxilla/5.0 (Window NT 10.0; Win64; x64) AppleWeb"}
res = requests.get(url,headers=headers)
res.raise_for_status() #정상코드


# res = requests.get("http://www.melon.com")
# res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
res.raise_for_status()

print(res.text)
#파일저장
with open("b.html","w",encoding="utf-8") as f:
    f.write(res.text)