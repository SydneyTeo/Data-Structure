# Uses python3
import sys

def get_change(amt):
    #write your code here
    coins = [10, 5, 1]  # must be sorted
    count = 0
    for coin in coins:
        count += amt // coin
        amt %= coin
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
