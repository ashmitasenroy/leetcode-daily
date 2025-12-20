n=int(input("Enter a number: "))
fact=1
for i in range(n):
    fact*=i+1
print("The factorial of", n, "is:", fact)