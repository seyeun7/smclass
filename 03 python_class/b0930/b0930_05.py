def add():
    print(10+9)
    a=10 # 지역변수:함수를 벗어나면 없어짐

# 자바스크립트 함수선언
# function add(){
# var i = 0; //지역변수
# }



# #문자열
# print("안녕 영어로는 \"hello\" 입니다. ")
# print('안녕 영어로는 "hello" 입니다. ')
#쌍따음표를 사용하고 싶을땐 쌍따음표 안에 쌍따음표는 역슬래시, 온따음표 안에 쌍따음표를 사용


# #불형
# a = (10>100)
# print(a)
# b = (10==10)
# print(b)
# print(type(b))

#사칙연산 수식
# + , - , * , / - 소수점이 있는 몫 , %-나머지, //- 정수형태 몫, * -제곱

# print(5+2) # 7
# print(5-2) # 3
# print(5*2) # 10
# print(5/2) # 2.5
# print(5%2) # 1
# print(5//2) # 2 - 정수형태몫
# print(5**2) # 25 -제곱
# print(3**2) # 3*3
# print(4**4) # 4*4*4*4


#
# a=0
# for i in range(1,11):  #10 : 10번 0, 10 : 0에서 9까지 i : 변수선언, range : 범위 얼마에서 어디까지 
#   a += i    # a = a + i
# print(a)

 
#4바이트 약 42억정도...

#for(var i=0;i<10;i++){
#}



# 두 수를 입력받아 더하기,빼기,곱하기,나누기를 출력하시오.
# num = int(input("숫자를 입력하세요"))
# num2 = int(input("숫자를 입력하세요"))

# print("{},{},{},{}".format(num+num2,num-num2,num*num2,num/num2))

# print(type(num+num2))
# print(type(num-num2))
# print(type(num*num2))
# print(type(num/num2))

# #0으로 나누면 에러가 남 division by zero
# #타입은 모두가 int 지만 나누기는 float가 된다