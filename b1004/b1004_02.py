import random

# 랜덤숫자 : 1-100
# random.randint(1,100)

# 10번 도전에서
# 입력한 숫자가 더 크면 작은 수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰 수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면 , 10번 도전에 실패했습니다. 랜덤숫자 :
# 도전에 성공했습니다. 랜덤숫자 : 

# r_num =random.randint(1,100)
# count = 0
# for i in range(10):
#     input_num = int(input("숫자를 입력하세요"))
#     if input_num > r_num:
#         print("입력한 숫자가 더 큽니다.")
#     elif r_num > input_num:
#         print("입력한 숫자가 더 작습니다.")
#     else:
#         print("도전에 성공했습니다. 랜덤숫자 :",input_num)
#         count = 1
#         break
# if count ==0:
#     print("10번 도전에 실패했습니다. 랜덤숫자 :",r_num)

r_num =random.randint(1,100)
i = 0       # 반복횟수 변수
count = 0   # 확인하는 변수
while(i<10):
    input_num = int(input(f"{(i+1)}번째 숫자를 입력하세요."))
    if r_num < input_num:
        print("입력한 숫자가 더 큽니다. 작은 수를 입력하세요.")
    elif r_num > input_num:
        print("입력한 숫자가 더 작습니다. 큰 수를 입력하세요.")
    else:
        print(f"정답입니다.. 랜덤숫자 : {r_num}")
        count = 1
        break
    i += 1
if count == 0:
    print(f"10번 도전에 실패했습니다. 랜덤숫자 : {r_num}")