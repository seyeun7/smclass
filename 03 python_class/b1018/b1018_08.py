class Student:
    count = 0
    students = []

    def __init__(self,name,kor,eng,math):
        Student.count += 1
        self.no = Student.count
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = (kor+eng+math)/3
        self.rank = 0
        Student.students.append(self)

    def __str__(self):
        return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}\t"

    def print(self):  # 딕셔너리 타입으로 리턴
        return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
s_t = ['no','name','kor','eng','math','total','avg','rank']  

while True:
    print("[ 학생성적 프로그램 ]")
    print("1. 학생성적입력")
    print("2. 학생성적출력")
    choice = int(input("원하는 번호를 입력하세요.>> "))

    if choice == 1:
        print(" [학생성적 입력]")
        name = input("이름을 입력하세요.")
        score = []
        for i in range(2,5):
            score.append(int(input(f"{s_title[i]}점수를 입력하세요.>>")))
        Student(name,*score)

        for s in Student.students:
            print(s)


# 1. 학생성적입력
# 이름,국어,영어,수학 -> 번호,국어,영어,수학,합계,평균,등수
# 클래스 1개가 생성이 되고
# 클래스의 참조변수(__str__) 출력을 해보세요.