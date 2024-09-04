height=int(input("enter height"))

if height>=3:
    print("can ride")
    age=int(input("enter age"))
    if age<12:
        print("pleaase pay 150")
    elif age<=18:
        print("please pay 250rs")
    else:
        print("please pay500rs")
else:    
    print("can't ride")
    print("bye")
        