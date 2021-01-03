# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    for i in range(1, n+1):
        if i > n:
            if n != 0:
                summands[len(summands)-1] += n

            return summands

        summands.append(i)
        n = n - i

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

