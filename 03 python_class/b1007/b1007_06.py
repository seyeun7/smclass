import random

# 25개 1차원 리스트

# 25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오.
a_list = [0]*20+[1]*5
random.shuffle(a_list)
print(a_list)

# [5,5] 2차원리스트에 a_list의 값을 입력한 후 출력하시오.

b_list = []
for i in range(5):
    a = []
    for j in range(5):
       a.append(a_list[5*i+j])  # -,1,2,3,.....24   # a_list 5개를 리스트에 추가
    b_list.append(a)              #a 리스트를 b_list리스트에 추가
print(b_list)

#[5,5] 출력
while True:
    for i in range(5):
        for j in range(5):
            print(b_list[i][j],end="\t")
        print()

    num = input("좌표를 입력하세요.(0,0)>> ")
    num2 = num.split(",")
    print(f"{num2} 좌표 값 : {b_list[int(num[0])][int(num2[1])]}")

# 0:20개, 1:5개 생성
# a_list = []
# for i in range(25):
#     if i<20:
#         a_list.append(0)
#     else:
#         a_list.append(1)