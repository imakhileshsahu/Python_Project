# n=5
# for i in range(0,n):
#     for j in range (i):
#        print("*",end="")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print("*",end="")
#     print()     
        
        
t=(10,40,50,70,90)
print(t)        
t=t+(20,)
print (t)
l=list(t)
l.append(3)
t=tuple(l)
print(t)