# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))

# def calc_fib(n):
#     F = []
#     F[0] = 0
#     F[1] = 1
#     for i in range (2, n, 1):
#         F[i] = F[i-1] + F[i-2]
#     return F[n]


# n = int(input())
# print(calc_fib(n))
