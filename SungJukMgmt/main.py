#main.py
import student_input
import student_cal
import student_output

print("Program is start")

student = {}
student_input.myinput(student) # call by reference
student_cal.cal(student)
student_output.output(student)

print("Program is over")