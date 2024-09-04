student_data=[
  {'name' : 'ram',
   'rollno.':10,
   'age':20,
   'course':'python'},
    {'name':'mohan',
     'rollno.':11,
     'age':30,
     'course':'java'}
     
]
def add_new_student(name,rollno,age,course_opted):
    new_student={}
    new_student['name']=name
    new_student['rollno.']=rollno
    new_student['age']=age
    new_student['course']=course_opted
    student_data.append(new_student)
    
add_new_student('shyam',22,18,'c++') 
print(student_data)   