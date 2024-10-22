# 반드시 외우기
import random

# 1-100 까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램 종료 하시오. break

### for 문
r_num = random.randint(1,100)
count = 0
for i in range(10):
    input_num = int(input("숫자를 입력하시오.")) #str -> int 타입으로 변경
    if r_num < input_num:
        print("입력한 숫자가 큽니다.")
    elif r_num > input_num:
        print("입력한 숫자가 작습니다.")
    else:
        print("정답입니다.정답번호 :",input_num)
        count = 1
        break
    # 10번 도전에서 실패 할 경우
if count == 0:
    print("10번 도전에 실패하셨습니다. 정답번호 : ",r_num) 
    


### while문
# i =0 # 초기값
# r_num = random.randint(1,100) # while 안에 있으면 돌때마다 랜덤숫자 같이 변경 그렇기때문에 while 문 밖에 있어야함
# count =0
# while i<10: # 조건식
#     input_num = int(input("숫자를 입력하시오.")) #str -> int 타입으로 변경
#     if r_num < input_num: # 비교구문
#         print("입력한 숫자가 큽니다.")
#     elif r_num > input_num:
#         print("입력한 숫자가 작습니다.")
#     else:
#         print("정답입니다.정답번호 :",input_num)
#         count = 1
#         break
#     i+=1 #증감식
#     # 10번 도전에서 실패 할 경우
# if count == 0:
#     print("10번 도전에 실패하셨습니다. 정답번호 : ",r_num) 

     