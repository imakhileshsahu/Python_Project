# import statistics 
# def mean_median_mode(list1):
#     return [statistics.mean(list1),statistics.median(list1),statistics.mode(list1)]

# print(mean_median_mode([2,3,45,67,4,32,4]))
 
 
 
def add(a,b):
     if a==0 & b==0:
         return 'none'
     else:
         return a+b
     
var1=int(input("eneter 1 var"))     
var2=int(input("eneter 2 var"))     
result=add(var1,var2) 
print(result)   