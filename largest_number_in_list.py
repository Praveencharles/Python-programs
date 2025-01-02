a=[]
N=int(input("enter the upper limit :"))
for i in range(1,N+1):
    element=int(input("enter the element :"))
    a.append(element)
print("the largest number in the list is :",max(a))