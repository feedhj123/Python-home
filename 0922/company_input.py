# 이한재
# 입력 프로그램
employee = {}  
def myinput(employee):
    try:
        employeenumber = int(input("사원번호 : "))
        if not (1 <= employeenumber < 100):
            raise ValueError("Error: please input an integer between 1 and 99")
        
        glevel = int(input("급 : "))
        if not (1 <= glevel < 10):
            raise ValueError("Error: please input an integer between 1 and 9")
        
        hlevel = int(input("호 : "))
        if not (1 <= hlevel < 10):
            raise ValueError("Error: please input an integer between 1 and 9")
        
        bonus = int(input("수당 : "))
        
        employee["employeenumber"] = employeenumber
        employee["glevel"] = glevel
        employee["hlevel"] = hlevel
        employee["bonus"] = bonus
    
    except ValueError as e:
        print(e)
myinput(employee)