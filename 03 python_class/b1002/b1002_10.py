fruit = []
while True:
    # strip() 앞쪽여백,뒤쪽여백 제거 trim ' 사과 ' -> '사과'  단 글자와 글자사이의 공백은 불가능 '사   과' -> '사   과'
    # replace(" ","") : 문자대체함수
    # search = input("과일이름을 입력하세요.(종료:x)").strip()
    search = input("과일이름을 입력하세요.(종료:x)").replace(" ","")
    if(search =='x'):
        break

    # if 항목 in 리스트 : 리스트에 해당 항목이 있다면 True를 반환
    # 입력된 과일이름을 리스트에 추가하시오.
    if search in fruit:
        print("같은 이름이 있습니다.")
        print("모든 과일이름 :",fruit)
    else:
        print(f"{search}을(를) 추가합니다.")
        fruit.append(search)
        print("모든 과일이름:",fruit)


# 반복 문을종료할때 : break
# while True:
#     break

# print("프로그램 종료")


# 무한 반복문은 while True 입력
# a=0
# while True:  #무한반복
#     print(a)
#     a += 1

# while (a<10):
#     a +=1
#     print(a)

# print("프로그램 종료")