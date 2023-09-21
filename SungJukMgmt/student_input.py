# 성적 입력 받음

def myinput(student):
    name = input("Enter Your Name : ")
    kor = int(input("Enter Your Korean : "))
    eng = int(input("Enter Your English : "))
    math = int(input("Enter Your Math: "))
    student["name"] = name
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math