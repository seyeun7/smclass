print("{} 평균 : {:.2f}"
.format("홍길동",(100+100+99)/3))
name = "홍길동"

### f 함수 소수점자리 출력
a = 1.12345
print(f"소수점 2자리 출력 : {a:.2f}")


print("출력이 됩니다.!!")

print("""\
1.언론 자율기구인 한국신문윤리위원회는 최근 SNS와 동영상 플랫폼의 콘텐츠 인용 
보도 시 통일된 출처 표기방식을 도입하기 위한 
‘SNS 등 저작물 출처 표기 가이드라인’을 마련해 26일 발표했다.
""")


# name = "홍길동"
# num = 100
# num2 = 100
# num3 = 99
# print("%s 합계 : %d" % (name,num+num2+num3))
# print("{} 합계 : {}".format(name,num+num2+num3)) #format은 {}
# print("%s 평균 : %.2f" % (name,(num+num2+num3)/3))
# print("{} 평균 : {:.2f}".format(name,(num+num2+num3)/3)) #{앞에 :를 넣기}

# # 숫자 : 12.12345 , 456.78940, 2.252525
# # 소수점 2자리 출력
# # 숫자 : 12.12, 456.79, 2.25
# print("숫자 : {:.2f},{:.2f},{:.2f}".format(12.12345 , 456.78940, 2.252525))
# #\n : 줄바꿈 \t 다음탭으로 이동 

# print("\*") #역슬래시 =뒤에를 문자로 인식해라
# print("안녕\n하세요.")
# print("안녕\t하세요.")

# print("언론 자율기구인 한국신문윤리위원회는 최근 SNS와 동영상 플랫폼의 콘텐츠 인용\n 보도 시 통일된 출처 표기방식을 도입하기 위한 ‘SNS 등 저작물 출처 표기 가이드라인’을 마련해 26일 발표했다.")
# print("""\ 
# 1.언론 자율기구인 한국신문윤리위원회는 최근 SNS와 동영상 플랫폼의 콘텐츠 인용 
# 보도 시 통일된 출처 표기방식을 도입하기 위한 
# ‘SNS 등 저작물 출처 표기 가이드라인’을 마련해 26일 발표했다.
# """) #공백을 제거할때 \ 를 쓴다