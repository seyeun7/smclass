#숫자맞추기
import random
r_num = random.randint(1,100)
count =0
for i in range(10):
    input_num = int(input("숫자를 입력하세요."))
    if r_num < input_num:
        print("입력한 숫자가 큽니다.")
    elif r_num > input_num:
        print("입력한 숫자가 작습니다.")
    else:
        print("정답입니다.정답번호:",input_num )
        count = 1
        break
if count == 0:
    print("10번 도전에 실패하셨습니다. 정답번호 : ",r_num) 
