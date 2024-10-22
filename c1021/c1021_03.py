# naver 파일저장. 리솜리조트 파일저장
import requests
# url = "https://www.resom.co.kr/resom/main/main.asp"
# url = "http://www.naver.com/"
# url = [
#     "http://www.naver.com/",
#     "http://www.resom.co.kr/resom/main/main.asp"
    
# ]

url = ["http://www.coupang.com/"]
headers = {"User-Agent":"Moxilla/5.0 (Window NT 10.0; Win64; x64) AppleWeb"}

for i in range(len(url)):
    res = requests.get(url[i],headers=headers)
    res.raise_for_status() #정상코드


    with open(f"c1021/{i}.html","w",encoding="utf-8") as f:
        f.write(res.text)

print("프로그램 종료!")

# 쿠팡페이지 저장
url = "http://www.coupang.com/"
headers = {"User-Agent":"Moxilla/5.0 (Window NT 10.0; Win64; x64) AppleWeb"}