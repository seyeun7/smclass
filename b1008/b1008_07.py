import operator

# zip()함수
# name = ["홍길동","유관순","이순신"]
# score = [100,90,95]
n_list = []
for n,s in zip(name,score):
    n_list.extend([n,s])
    print(n,":",s)

print(n_list)

# numList = []
# # 리스트 1,2,3,4,5
# # 리스트에 추가방법
# for i in range(5):
#     numList.append(i+1)

# print(numList)

# #1줄 for문을 1줄로 사용해서 처리
# # 리스트 내포 , 컴프리헨션
# nList = [i+1 for i in range(5)]
# print(nList)

# a_list = [str(i*i) for i in range(5)]
# print(a_list)

# # 정수형 -> 문자열
# b_list = [str(i) for i in range(5)]
# print(b_list)

# # 문자열 -> 정수형
# c_list = ["5","9","0","3","2"]
# cc_list = [int(i) for i in c_list]
# print(cc_list)

# d_str = "1,2,23,5,9"
# d_sp = [int(i) for i in d_str.split(",")]
# print(d_sp)

# # 문자열을 받아 
# score  = input("좌표를 입력하세요(0>0) >>")
# sc = [int(i) for i in score.split(".")]
# print(score)
# print(sc)



# students = [
#   {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
#   {"no":1,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
#   {"no":1,"name":"이순신","kor":90,"eng":90,"math":90,"total":271,"avg":90.33,"rank":0},
#   {"no":1,"name":"강감찬","kor":60,"eng":65,"math":64,"total":192,"avg":64.00,"rank":0},
#   {"no":1,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
# ]

# # 리스트 딕셔너리 정렬
# for s in students:
#     print(s)

# x =list(students)
# print(type(x))

# print(students)
# x = sorted(students.items())
# students.sort()
# print("-"*50)
# print(students)



# nameDic = {'홍길동':100,'유관순':80,'이순신':95,'강감찬':82,'김구':97}

# key - nameDic.keys()
# value - nameDic.values()
# key,value - nameDic.items() 
# print(nameDic)
# key =[0], value - [1]
# (key,value) : [0,1]

# lambda x:x[0], lambda x:x[1]
# nameDic = sorted(nameDic.items(),key=lambda x:x[0]) # 람다식구현
# nameDics = sorted(nameDic.items(),key=operator.itemgetter(1),reverse=True) #[1]번째로 역순정렬
# nameDics = sorted(nameDic.items(),key=operator.itemgetter(1))              #[1]번째로 순차정렬

# nameDic = sorted(nameDic.items())               #[0]번째로 순차정렬
# nameDic = sorted(nameDic.items(),reverse=True)  #[0]번째로 역순정렬
# print("-"*50)
# print(nameDic)