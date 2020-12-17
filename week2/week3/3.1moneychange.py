# Uses python3


def get_change(amt):
    #write your code here
    coins = [10, 5, 1]  # must be sorted
    count = 0
    for coin in coins:
        # Update count with the the number of coins 'are held' in the amount.
        count += amt // coin
        # Put remainder to the residuary amount.
        amt %= coins

    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
