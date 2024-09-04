import os
def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    return a/b
def modulus (a,b):
    return a%b
operatios_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "%":modulus
    
}
def calculator():
  number1=int(input("Enter first number:"))
  for symbol in operatios_dict:
      print(symbol)
    
  continue_flag=True
  while continue_flag:    
    op_symbol=input("Pick an operation :  ")  
    number2=int(input("Enter next number:"))
    calculator_function=operatios_dict[op_symbol]#add
    output=calculator_function(number1,number2)
    print(f"{number1}{op_symbol}{number2} = {output}")
   
    should_continue=input(f"Enter 'y' to continue calculation with {output} or 'n' to start new calculation or 'x' to exit").lower()
    if should_continue=='y':
       number1=output
    elif should_continue=='n':
        continue_flag=False
        os.system('cls')
        calculator()
    else:
       continue_flag=False
       print("Bye")
calculator()     
