#  출력 파트

def output(student):
    print(f"이름은 = {student['name']}\t 국어성적은 = {student['kor']}\t 영어 성적은 = {student['eng']}\t")
    print(f"수학 성적은 = {student['math']}\t 총합계는 = {student['total']}\t 평균 점수는 = {student['avg']:.2f}\t")
    print(f"최종 학점은 = {student['grade']}")