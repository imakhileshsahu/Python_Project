student_marks={
    'akhil':92,
    'rohit':78,
    'indu ':56,
    'ruchi':41,
    'mohit':99,
    'akshat':34
    
}
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]="A"
    elif marks>70:
        student_grades[student]="B+"
    elif marks>60:
        student_grades[student]="B"
    elif marks>50:
        student_grades[student]="C"
    elif marks>40:
        student_grades[student]="D"
    else:
        student_grades[student]="F"
print(student_grades )