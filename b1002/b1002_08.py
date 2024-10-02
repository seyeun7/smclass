# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수 
# find - 데이터가 있는 위치, 없으면 -1
# index - 데이터가 있는 위치, 없으면 에러

fruit ="사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는지 위치를 모두 출력하시오.
search = input("과일 이름을 입력하세요.")
print("모든 글자 :",fruit)
idx = 0
if fruit.count(search)>0:
    print(f"{search} 글자가 있습니다.")
    for i in range(fruit.count(search)): 
        print(f"{search} 글자가 있는 위치 :",fruit.find(search,idx))  # find(찾을문자, 시작 index, 끝 index)
        idx = fruit.find(search,idx)+1
else:
 print(f"{search}(이)라는 글자는 없습니다.")


# count : 문자열 내에 해당숫자개수 확인
# fruit ="사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# # 과일이름을 입력받아, 과일이름이 있습니다. 과일검색 개수 :\
# # 없으면 없습니다.

# search = input("과일을 입력하세요.")
# if search in fruit:
#     print(f"{search}은(는)있어요.")
#     print("과일검색개수: {}".format(fruit.count(search)))
#     #print(fruit.find(search))
#     #print(fruit.index(search))  # 배가 있는지 위치의 index
# else:
#     print(f"{search}은(는)없습니다.")
    #print(fruit.find(search)) # 없을때 에러가 나오지않고 -1로 표시된다
    #print(fruit.index(search)) #없을때는 사용하기가 힘듬
    #index보다는 find 를 사용하는걸 권장한다.


#print(fruit.count('사과'))



#count : 리스트에서 개수확인
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))



# fruit = ['사과','배','딸기','포도','복숭아']
# #글을 입력받아 입력한 과일이 있으면 있어요, 없으면 없어요.

# search = input("과일을 입력하세요.")
# if search in fruit:
#     print(f"{search}있어요.")
# else:
#     print(f"{search}없어요.")


# fruit = "사과,배,달기,포도"  #배열형태도 가능 문자열도 리스트형태로 가능
# if '배' in fruit:
#     print("배라는 글자가 있어요.")
# else:
#     print("배라는 글자가 없어요.")


# fruit = ['사과','배','딸기','포도','배']
# if '배' in fruit:  # 1번의 비교로 있는지 확인
#     print("배가 있어요.")
# else:
#     print("배가 없어요.")