import random
user_choice=int(input("enter your choice: Type 0 for rock ,1 for paper,2 for scissor."))
if user_choice>=3 or user_choice<0:
    print("you enter invalid number,you lose.")
else:
    comp_choice=random.randint(0,2)
    print("computer chose:")
    print("comp_choice")
    if comp_choice==user_choice:
      print("it is a draw")
    elif comp_choice==0 and user_choice==2:
      print("you win")
    elif user_choice==0 and comp_choice==2:
      print("you lose")  
    elif comp_choice>user_choice:
     print("you lose") 
    elif user_choice>comp_choice:
     print("you win")
