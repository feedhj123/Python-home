cal = {'Jan' : 31 , 'Feb' : 28, 'Mar' : 31 , 'Apr' : 30 , 'May' :31 , 'Jun' : 30 , 'Jul' : 31 , 'Aug' : 31 , 'Sep': 30, 'Oct' : 31 , 'Nov': 30,'Dec' : 31 }
cal_list = list(cal.keys())
count = 0
# 현재 년도 입력 받기
year = int(input('현재 년도를 입력해주세요 : '))
# 윤년인 경우 2월은 29일까지로 설정 
if year & 4 == 0 :
    cal['Feb'] = 29
# 달력의 월 출력
for i in range(0,12):
    print(cal_list[i],end = '\n')
# 달력의 일 출력
    for j in range(1,(cal[f'{cal_list[i]}']+1)):
        print(j, end='\t')
        count +=1
        if count % 7 ==0:
            print()
    print()
