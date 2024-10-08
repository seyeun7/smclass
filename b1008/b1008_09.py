# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":1,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":1,"name":"이순신","kor":90,"eng":90,"math":90,"total":271,"avg":90.33,"rank":0},
  {"no":1,"name":"강감찬","kor":60,"eng":65,"math":64,"total":192,"avg":64.00,"rank":0},
  {"no":1,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
choice = 0 # 전역변수
chk = 0 # 체크 변수
count = 1 # 성적처리
stuNo = len(students) # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 # 성적처리변수

# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  if choice == "1":
        while True:
            print("[학생성적 입력 ]")
            # 학생성적 직접 입력
            no = stuNo + 1 # 리스트 = 학생수
            name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
            if name == "0":
                print("성적입력을 취소합니다.")
                print()
                break
            kor = int(input("국어점수를 입력하세요."))
            eng = int(input("영어점수를 입력하세요."))
            math = int(input("수학점수를 입력하세요."))
            total = kor+eng+math
            avg = total/3
            rank = 0
            ss = { "no":no,"name":name,"kor":kor,"eng":eng,
                  "math":math,"total":total,"avg":avg,"rank":rank}
            students.append(ss)
            stuNo += 1 # 학생수 1증가
            print(f"{name} 학생 성적이 저장되었습니다!")
            print()
            
  elif choice == "2":
       print("[ 학생성적 출력 ]")
       for s in students:
            print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}\t")
       print()
  
  elif choice == "3":
     print("[ 학생성적수정 ]")
     name = input("찾고자 하는 학생의 이름을 입력하세요.")
     chk = 0
     for s in students:
         if s["name"] == name:
             print(f"{name} 학생을 찾았습니다.")
             print()
             print("[ 수정 과목을 선택 ]")
             print("1. 국어점수")
             print("2. 영어점수")
             print("3. 수학점수")
             choice = input("원하는 번호를 입력하세요.>> ")
             if choice =="1":
                 print("이전 국어점수 : {}".format(s["kor"]))
                 s["kor"] = int(input("변경된 국어점수 : "))
             elif choice =="2":
                 print("이전 영어점수 : {}".format(s["eng"]))
                 s["eng"] = int(input("변경된 영어점수 : "))
             elif choice =="3":
                 print("이전 수학점수 : {}".format(s["math"]))
                 s["math"] = int(input("변경된 수학점수 : "))
             s["total"] = s["kor"]+s["eng"]+s["math"]
             s["avg"] =  s["total"]/3
            

                 


  elif choice == "7":
    while True:
        print("[학생성적 정렬]")
        print("1. 이름으로 순차정렬")
        print("2. 이름으로 역순정렬]")
        print("3. 합계 순차정렬")
        print("4. 합계 역순정렬")
        print("5. 역순 순차정렬")
        print("0. 이전페이지 이동")
        print("-"*40)
        choice = input("원하는 번호를 입력하세요.>> ")

        if choice == 1:
           students.sort(key=lambda x:x['name'])
        elif choice == 2:
           students.sort(key=lambda x:x['name'],reverse=True)
        elif choice == 0:
            print("이전페이지로 이동합니다.")
            break
            
        
        print("정렬이 완료되었습니다.")





# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할 것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.

# no = 1
# name = input("학생이름을 입력하세요")
# kor = int(input("국어점수를 입력하세요."))
# eng = int(input("영어점수를 입력하세요."))
# math = int(input("수학점수를 입력하세요."))
# total = kor+eng+math
# avg = total/3
# rank = 0

# n_dic = ("번호")