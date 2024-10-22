# if - else
# if elif else
# 100~98 A+ / # 97~94 A / # 93~90 A-
# 89~88 B+ / # 87~84 B  / # 83~80 B-
# 70점대 C / # 60점대 D /# 60점 미하 F
num =int(input("점수를 입력하세요."))
score = ""
if 90<=num:
    score = "A"
    if 98<= num:
        score += "+"
    elif 90<= num <=93:
        score += "-"
elif 80<= num:
    pass
#중첩if문

# if 98<= num <=100:
#     print("A+입니다.")
# elif 94<= num:
#     print("A입니다.")
# elif 90<= num:        #뒤에 다음 범위가 있기때문에 큰 숫자 범위는 없어도 괜찮음
#     print("A-입니다.")
# elif 88<= num:
#     print("B+입니다.")
# elif 84<= num <=87:
#     print("B입니다.")
# elif 80<= num <=83:
#     print("B-입니다.")
# elif 78<= num <=79:
#     print("C+입니다.")
# elif 74<= num <=77:
#     print("C입니다.")
# elif 70<= num:
#     print("C-입니다.")
# elif 68<= num <=69:
#     print("D+입니다.")
# elif 64<= num <=67:
#     print("D입니다.")
# elif 60<= num:
#     print("D-입니다.")
# elif num <60:
#     print("F입니다.")




#숫자를 입력받아
# 3,4,5 - 봄, 6,7,8-여름 9,10,11-가을, 12,1,2 - 겨울입니다. 
# 그 외 숫자는 잘못된 월이 입력되었습니다. 출력하시오
# s = int(input("숫자를 입력하세요."))
# if  3<= s <=5:  # 3<=s and s<=5
#     print("봄입니다.")
# elif  6<= s <=8:
#     print("여름입니다.")
# elif  9<= s <=11:
#     print("가을입니다.")
# elif  1<= s <= 2 or s==12:
#     print("겨울입니다.")
# else :
#     print("잘못된 월이 입력되었습니다.")



#입력한 숫자가 10(포함)보다 작거나, 100(포함)보다 클때 정답입니다. 오답입니다.
# num = int(input("숫자를 입력하세요."))
# if num<=10 or num>=100:
#     print("정답입니다.")
# else :
#     print("오답입니다.")


# 입력한 숫자가 1(포함)보다 크고 10(포함)보다 작을때만 
# 1 <= x <= 10
# 정답입니다. 오답니다.
# num = int(input("숫자를 입력하세요."))
# if 1<= num <=10: # 파이썬에서만 가능하만 구문 다른 프로그램에선 에러나옴
#     print("정답입니다.")
# else :
#     print("오답입니다.")


# 입력한 숫자가 짝수인지, 홀수인지 출력하시오.
# num =  int(input("숫자를 입력하세요."))
# if num%2 == 0:
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")