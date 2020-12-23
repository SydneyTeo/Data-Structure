# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, b):
        first = a * l
        if b % first == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = input()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
