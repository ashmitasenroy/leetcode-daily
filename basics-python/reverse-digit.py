def numrev(n):
    s=str(n)
    rev=""
    for i in s:
        rev=i+rev
    return int(rev)

n=int(input("Enter a number: "))
print("The reverse of the number is:", numrev(n))

#withouut-using-string

n=int(input("Enter a number: "))
rev=0

while n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
print("The reverse of the number is:", rev)