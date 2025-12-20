#decreasing-pattern
    
n=int(input("Enter a number: "))

for i in range(n):
    for j in range(i,n):
        print("*", end="")
        
    print()