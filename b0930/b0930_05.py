# 두 수를 입력받아 더하기,빼기,곱하기,나누기를 출력하시오.
num = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))
print("{},{},{},{}".format(num+num2,num-num2,num*num2,num/num2))
print(type(num+num2))
print(type(num-num2))
print(type(num*num2))
print(type(num/num2))
#0으로 나누면 에러가 남 division by zero
#타입은 모두가 int 지만 나누기는 float가 된다