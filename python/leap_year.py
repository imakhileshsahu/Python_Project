yrs=int(input("enter year"))

if(yrs%4==0):
    if yrs%100==0:
        if yrs%400==0: 
            print("leap year")
        else:
            print("not leap")
    else:
        print("leap year")
else:
    print("not a leap year")        
            

