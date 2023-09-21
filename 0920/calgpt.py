cal = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
cal_list = list(cal.keys())

# 현재 년도 입력 받기
year = int(input('현재 년도를 입력해주세요: '))

# 윤년인 경우 2월은 29일까지로 설정
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    cal['Feb'] = 29

# 달력 출력
first_day_of_week = 0  # 첫 날의 요일을 초기화
for i in range(0, 12):
    month = cal_list[i]
    days_in_month = cal[month]
    
    # 월 이름 출력
    print(f'{year}년 {month}')
    
    # 요일 출력
    print('일\t월\t화\t수\t목\t금\t토')

    # 시작 요일까지 빈 칸 출력
    for _ in range(first_day_of_week):
        print('\t', end='')

    day_of_week = first_day_of_week

    # 날짜 출력
    for j in range(1, days_in_month + 1):
        print(j, end='\t')
        day_of_week += 1
        if day_of_week % 7 == 0:
            print()  # 주 단위로 줄바꿈

    # 다음 월을 위해 시작 요일 업데이트
    first_day_of_week = day_of_week % 7

    # 월 출력 후 한 줄 띄우기
    print()
