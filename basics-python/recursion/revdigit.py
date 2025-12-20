def rev_num(n, rev=0):
    if n == 0:
        return rev
    return rev_num(n // 10, rev * 10 + n % 10)

print(rev_num(12345))  
