students =[]
s_title = ["번호","이름","국어","영어","수학","합계","평균","등수"]
choice = 0
stuNo = 0
chk = 0

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  if choice == "1":
        print("[학생성적 입력]")
        no = stuNo + 1
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
        students.append([no,name,kor,eng,math,total,avg,rank])
        stuNo += 1
        print(f"{name} 학생 성적이 저장되었습니다.")
        print()
  elif choice == "2":
       print("                  [학생성적 출력]")
       for title in s_title:
           print(f"{title}\t",end="")
       print()
       print("-"*60)
       for s in students:
           print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]}\t{s[7]}\t")
       print()
  elif choice == "3":
      print("[학생성적 수정]")
      name = input("찾고자 하는 학생의 이름을 입력하세요.")
      chk = 0
      for s in students:
          if s[1] ==name:
              print(f"{name} 학생을 찾았습니다.")
              print()
              print("[ 수정 과목을 선택 ]")
              print("1. 국어점수")
              print("2. 영어점수")
              print("3. 수학점수")
              choice = input("원하는 번호를 입력하세요.>> ")
              if choice == "1":
                  print("이전 국어점수 : {}".format(s[2]))
                  s[2] = int(input("변경 국어점수 :"))
              elif choice == "2":
                  print("이전 영어점수 : {}".format(s[3]))
                  s[3] = int(input("변경 영어점수 :"))
              elif choice == "3":
                  print("이전 수학점수 : {}".format(s[4]))
                  s[4] = int(input("변경 수학점수 :"))
                

          

       