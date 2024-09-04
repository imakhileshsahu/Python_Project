height=int(input("enter height"))

if height>=3:
    print("can ride")
    age=int(input("enter age"))
    if age<12:
        bill=150
        print("Ticket Price pay 150rs")
    elif age<=18:
        bill=250
        print("Ticket Price pay 250rs")
    else:
        bill=500
        print("Ticket Price pay500rs")
    want_photo=input("do you want to take photo(y/N)")
    if want_photo=='y' or want_photo=='Y':
       bill=bill+50 
    print(f"your total bill is {bill}")   
else:    
    
    print("can't ride")
    print("bye")