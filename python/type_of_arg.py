# def greet(name,dept):
#     print(f"hi {name}")
#     print(f"are you from {dept} department")
# greet("jenny",dept="cs")# positional argument
# greet (name="jenny",dept="cs")    #keyword arg



# # default
# def greet(name,dept="cs"):
#     print(f"hi {name}")
#     print(f"are you from {dept} department")
# greet("jenny")    

# variables length argumwnt
# #positional arg
# def add(*numbers):
#    c=0
#    for i in numbers:
#        c=c+i
#    print (f"sum{c}") 
# add(5,4,7)
# add(1,2,3,4,5,6)     
       
#keyword arg
def info_person(**kwargs):
    for key,value in kwargs.items():
        print(key ,value)
info_person(name="Ram",age=30,dept="cse")
info_person(name="shyam",dept="cse")        
