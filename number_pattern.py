x=int(input())
y=int(input())
for i in range(0,x*2+y,y):
    if x-i>0:
        a=x-i
        print(a)
    elif x-i<0:
        a=x-i
        a=a+a*-2
        print(a)