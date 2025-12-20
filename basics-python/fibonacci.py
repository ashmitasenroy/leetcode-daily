n=int(input("Enter a number: "))
a,b=0,1
print("The Fibonacci series is:")
for i in range(n):
    print(a)
    a, b=b, a+b