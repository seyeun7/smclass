# 10은 2의 배수입니다.
print("%d는 %d의 배수입니다." % (10,2))
a = 10
b = 2
#print(a+"은" + b+"의 배수입니다.") 에러,  타입이 다르기 때문에 불가능 
print(a,b)

#출력 자리수
print("%d" % b)
print("%5d" % b) #공간 5자리를 확보
print("%05d" % b) #빈칸을 0으로 채움


#001 010 100.000 3번 프린트를 사용해서 출력
num = 1
num2 = 10
num3 = 100

# print("%03d" % num)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %.2f" %(num,num2,num3))

# print("%5d" % (-10))

# 소수점 둘째자리까지 출력하시오. 758.12345678
print("%.2f" % (758.12345678))

# 총 10자리, 빈칸은 0으로 채워 소수점 2자리 까지 출력하시오. 25.05
#-> 소수점도 1자리를 차지한다
print("%013.2f" %(25.05))

#변수 150.15를 정수,실수,문자열로 출력하시오
print("%d" % (150.15)) 
print("%f" % (150.15)) #소수점은 6자리까지만 나타남
print("%s" % (150.15)) 
#print("안녕하세요." + 10) - 타입이 다른 것은 + 할수가 없음
print(10+10)
print("안녕"+"hello")
print("안녕하세요 : ",10) # 쉼표로 구분하면 가능하다 (하지만 약간의 띄어쓰기가 있음)

#*을 10개 출력하시오.
print("*"*10)

print("%5.1f" % (123456789.123)) #양수부분은 자리수와 상관없이 모두 출력이 됨



# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))


# 사용표시 %s:문자열, %c:문자1개, %f:실수, %d:정수
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# # 홍길동 총합 : 299, 평균 : 99.66666 #.2 자리수 표시

# print("%s 총합 : %d, 평균 : %.2f" % (name,kor+eng+math,(kor+eng+math)/3)) 



 
#### print사용형태 ####
#print 1.쉼표,%,format,f
# print(a,"은",b,"의 배수입니다.") #같은 타입끼리만 더하기 빼기 곱하기 나누기가 가능
# print("%d은 %d의 배수입니다." % (a,b))
# print("{}은 {}의 배수입니다.".format(a,b))
# print(f"{a}은 {b}의 배수입니다.")