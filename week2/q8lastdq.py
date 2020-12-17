from sys import stdin

def fib(n):
    a,b = 0, 1
    for i in range(2,n+1):
        c = (a+b)%10
        a, b = b, c 
    return c

n = int(input())
if n<=1:
    print(n)  
    exit()

less_than_n = n%60
less_than_n_plus_1 = (n+1)%60

if less_than_n <= 1:
    a = less_than_n
else:
    a = fib(less_than_n)

if less_than_n_plus_1 <= 1:
    b = less_than_n_plus_1
else:
    b = fib(less_than_n_plus_1)

print((a*b)%10)