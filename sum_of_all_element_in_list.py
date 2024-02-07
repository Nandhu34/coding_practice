lst=[]
sum=0
multiply=1
n=int(input("enter the limit"))
for i in range(0,n):
    lst.append(int(input(f"enter {i} element ")))
for element in lst:
    sum=sum+element
    multiply=sum*multiply
print("sum of element is ",sum)
print("multiply of element is ",multiply)
#get sum and multiply of all value in list in python
