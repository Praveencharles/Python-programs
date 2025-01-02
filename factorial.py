def factorial(num):
    if num<0:
        return 0
    elif num==0 or num==1:
        return 1
    else:
        fact=1 
        while(num>1):
            fact=fact*num
            num=num-1
        return fact
n=int(input("enter the number :"))
print("factorial of the ",n," is: ",factorial(n))