numbers=input ("enter no.")
numbers_list=numbers.split()
count=0
for number in numbers_list:
    count+=1
print(f"the lenght of the list is :{count}")
for i in range(count):
    numbers_list[i]=int(numbers_list[i]) 
maximum_number=numbers_list[0]
for number in numbers_list:
    if number> maximum_number:
        maximum_number=number
print(f"the maximum number is:{maximum_number}")               

