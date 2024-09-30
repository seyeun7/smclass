# name,kor,eng,math,total,avg 출력
# input으로 입력을 받아
# 홍길동,100,100,99,합계,평균 1줄에 출력하시오. 평균은 소수점 2자리까지

name = input("이름을 입력하세요.")
kor = input("국어점수을 입력하세요.")
#kor = int(input("국어점수을 입력하세요."))
eng = input("영어점수을 입력하세요.")
math = input("수학점수을 입력하세요.")
print(type(kor))
total = int(kor)+int(eng)+int(math)  #문자여렝서 정수형으로 타입 변경
avg = total/3
print("{},{},{},{},{},{:.2f}".format(name,kor,eng,math,total,avg))
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")



# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b) # 문자연결 연산자 100200
# print(int(a)+int(b)) # 타입변경
# name = "홍길동"
# # print(int(name)) #문자를 숫자로는 변경이 불가능함. 문자 -> 숫자 는 가능
# c = "3.14"
# print(int(float(c))) #실수형으로 변경후 다시 정수형으로 변경
# # print(int(c)) #문자실수형은 정수로 바로 변경은 불가
# print(str(c)) #실수형을 문자열로 변경

# d = "True"
# print(bool(d)) # 문자불형을 불형으로 변경

# # 타입 변경 - str,float,int,bool



# name = "홍길동"
# print(type(name))

# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True #True,False 대문자로 넣어야 함.
# print(type(a_bool))


# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)



# 변수 : 어떠한 값을 저장하는 메모리 공간
# 변수 선언은 그릇을 준비하는 것
# 변수를 선언하지 않아도 되지만 긴 코드를 작성할 때는 사용될 변수를 미리 계획적을 준비하면 좋음
# boolVar 불형 true False inVar 정수형 100 floatVar 실수형 123.45 strbVar 문자형 "안녕?"
# Type() 함수를 사용하면 변수가 boll(불형) int(정수) float(실수) str(문자열)
# 변수명 규칙 대소문자 구분 myVar MyVar는 다른 변수임
# 문자 숫자 언더(_)를 포함할수있다 숫자로 시작하면 안된다. (var2(o) _var(o) var_2(o) 2var(x))

