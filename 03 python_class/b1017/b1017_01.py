subject = ["국어","영어","수학","과학","역사"]
score = []

while True:
    print("1.과목추가")
    print("0.종료")
    choice = input("원하는 번호를 입력하세요.>>")
    if choice == "1":
        s_input = input("과목을 추가하세요.>>")
        subject.append(s_input)
    elif choice == "0":
        break

for i in range(len(subject)):
    score.append(int(input(f"{subject[i]}점수를 입력하세요.>> ")))

sum = 0
for i in range(len(subject)):
    print(f"{subject[i]}:",score[i])
    sum+= score[i]
print("합계 :",sum)


# num1 = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))
# num4 = int(input("과학점수를 입력하세요."))
# num5 = int(input("역사점수를 입력하세요."))
# print("국어 :",num1)
# print("영어 :",num2)
# print("수학 :",num3)
# print("과학 :",num4)
# print("역사 :",num5)
# print("합계 :",num1+num2+num3+num4+num5)




# # 함수선언
# def output(subject):
#     # 출력
#     print("과목")
#     print("-"*20)
#     for s in subject:
#         print(s)


# while True:
#     print("[ 과목 생성 프로그램]")
#     s_input = input("원하는 과목을 입력하세요.>> ")
#     # list - append
#     subject.append(s_input)
#     output(subject)  # 출력함수호출




# a = 10
# b = 20
# c = 30

# # a에 함수는 사용해서, a+b+c의 합을 입력해서 출력하세요.
# def add(a,b,c):  # 지역변수
#     a = a+b+c
#     print(a)
    

# add(a,b,c)  # 전역변수
# print(a) 



# a = 10
# b = 20
# sum = 0

# # 함수선언
# def add(a,b):
#     return a+b

# sum = add(a,b)  # 함수호출
# print("a+b 합계 : ",sum) 


# # 파이썬은 위에서 아래로 진행이 되어서 호출이 밑에 있어야함
# a = 10   # 전역변수   
# # 함수선언
# def func(a):
#     print("함수내 a :",a)
#     a += 50
#     return a # 변수는 리턴에서 받아야한다
#     # global a # 전역변수를 가져옴.
#     # a = 50  # 지역변수 - 함수를 종료하면 모두 제거됨.

# # 함수호출
# a = func(a)
# print("함수밖 a : ",a)



# subject = ["국어","영어"]

# # 함수선언
# def output(subject):
#     # 출력
#     print("과목")
#     print("-"*20)
#     for s in subject:
#         print(s)


# while True:
#     print("[ 과목 생성 프로그램]")
#     s_input = input("원하는 과목을 입력하세요.>> ")
#     # list - append
#     subject.append(s_input)
#     output(subject)  # 출력함수호출


    # 과목
    # -------
    # 국어
    # 영어
    # 수학