money = 175987
print("50000원 개수 :",money//50000)
print("10000원 개수 :",(money%50000)//10000)
print("5000원 개수 :",(money%50000)%10000//5000)
print("1000원 개수 :",(money%50000)%10000%5000//1000)
print("500원 개수 :",(money%50000)%10000%5000%1000//500)
print("100원 개수 :",(money%50000)%10000%5000%1000%500//100)
print("50원 개수 :",(money%50000)%10000%5000%1000%500%100//50)
print("10원 개수 :",(money%50000)%10000%5000%1000%500%100%50//10)

money2 = 9870
print("5000원 개수 :",(money%50000)%10000//5000)
print("1000원 개수 :",(money%50000)%10000%5000//1000)
print("500원 개수 :",(money%50000)%10000%5000%1000//500)
print("100원 개수 :",(money%50000)%10000%5000%1000%500//100)
print("50원 개수 :",(money%50000)%10000%5000%1000%500%100//50)
print("10원 개수 :",(money%50000)%10000%5000%1000%500%100%50//10)

money3 = 590
print("500원 개수 :",(money%50000)%10000%5000%1000//500)
print("100원 개수 :",(money%50000)%10000%5000%1000%500//100)
print("50원 개수 :",(money%50000)%10000%5000%1000%500%100//50)
print("10원 개수 :",(money%50000)%10000%5000%1000%500%100%50//10)




str1 = input("문자를 입력하세요.")
a = len(str1) # 문자의 길이 = length


# a = int(input("숫자를 입력하세요.")) #input은 무조건 문자이기때문에 타입을 꼭 변경해줘야함
if a==5:
    print("a는 5입니다.")
elif a==4: # = else if
    print("a는 4입니다.")
elif a==3:
    print("a는 3입니다.")
else:
    print("a 숫자는 2이하입니다.")



# money = 175987
# # 50000, 10000,5000,1000,500,100,50,10
# #50000
# print("50000원 개수 :",money//50000)
# print("10000원 개수 :",(money%50000)//10000)
# print("5000원 개수 :",(money%50000)%10000//5000)
# print("1000원 개수 :",(money%50000)%10000%5000//1000)
# print("500원 개수 :",(money%50000)%10000%5000%1000//500)
# print("100원 개수 :",(money%50000)%10000%5000%1000%500//100)
# print("50원 개수 :",(money%50000)%10000%5000%1000%500%100//50)
# print("10원 개수 :",(money%50000)%10000%5000%1000%500%100%50//10)



# money = 780
# # 500 -1
# print("500원 동전개수 :",money//500)
# # 100 -2
# print("100원 동전개수 :",(money%500)//100)
# # 50 -1
# print("50원 동전개수 :",(money%500)%100//50)
# # 10 -3
# print("10원 동전개수 :",(money%500)%100%50//10)