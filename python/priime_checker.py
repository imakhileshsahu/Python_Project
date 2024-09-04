import math 
def prime_checker(number):
    is_prime=True
    if number ==1:
       is_prime=False
    for i in range(2,math.ceil(number/2)+1):
        if number%i==0:
            is_prime=False
    if is_prime:
        print("prime no.")
    else:
        print("not prime")
n =int(input("enter a number \n"))
prime_checker(n)
list=           
                    
    