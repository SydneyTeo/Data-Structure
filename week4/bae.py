# Uses python3
import sys
sys.setrecursionlimit(5000)
dict = {}

def get_majority_element(a, left, right):
    if left == right:
        if a[left] in dict:
            dict[a[left]] += 1
        else:
            dict[a[left]] = 1
        
        for i in dict.values():
            if i > n//2:
                return i

    mid = (left + right)//2

    if len(a)%2 != 0:
        #odd
        if a[mid] in dict:
            dict[a[mid]] += 1
        else:
            dict[a[mid]] = 1

        get_majority_element(a, left, mid)
        get_majority_element(a, mid+2, right)

    elif len(a)%2 == 0:
        #even
        get_majority_element(a, left, mid)
        get_majority_element(a, mid+1, right)

    

if __name__ == '__main__':
    input = input()
    n, *a = list(map(int, input.split()))

    if get_majority_element(a, 0, n) == -1:
        print(0)
    else:
        print(1)
