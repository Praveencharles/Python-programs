n=int(input("enter the value of n :",))
print(n)
sq=0
sum=0
for i in range(1,n+1):
    sq=sq+(i*i)
    print(sq,end=' ')
print('\n')
for i in range(1,n+1):
    sum=sum+i
    print(sum,end=' ')