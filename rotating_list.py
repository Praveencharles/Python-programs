a=[1,2,3,4,5,6,7,8]
n=int(input("enter the position to be rotated :"))
b=(a[-n:]+a[:-n])
print("list \n",a,"rotated list \n",b)