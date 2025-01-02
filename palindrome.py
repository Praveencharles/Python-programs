def plain(x):
    return x==x[::-1]
x=input("enter a string :")
y=plain(x)
if y:
    print("palindrome")
else:
    print("not palindrome")