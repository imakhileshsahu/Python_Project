name1=input("enter name1")
name2=input("enter name2")

com_str = name1+name2

lowercasestring=com_str.lower()

t=lowercasestring.count('t')
r=lowercasestring.count('r')
u=lowercasestring.count('u')
e=lowercasestring.count('e')
true=t+r+u+e


l=lowercasestring.count('l')
o=lowercasestring.count('o')
v=lowercasestring.count('v')
e=lowercasestring.count('e')
love=l+o+v+e

love_score=int(str(true)+str(love))

if love_score<10 or love_score>90:
    print(f"your scrore is{love_score} and you go together kie coke and mentos")
elif love_score>=34 and love_score<=50:
    print(f"your scrore is{love_score} and your are alright together")
else:
    print(f"your score is{love_score}")