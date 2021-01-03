# Uses python3
import sys

#mergesort
def get_majority_element(a, left, right):
    if left == right:
        return [a[left]]

    mid = (left+right)//2
    B = get_majority_element(a, left, mid)
    C = get_majority_element(a, mid+1, right)
    sortedArray = merge(B, C)

    return sortedArray


#merge called within mergesort
def merge(left_array, right_array):
    sorted = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] > right_array[right_index]:
            sorted.append(right_array[right_index])
            right_index += 1

        elif left_array[left_index] <= right_array[right_index]:
            sorted.append(left_array[left_index])
            left_index += 1

    if left_index < len(left_array):
        for i in left_array[left_index:]:
            sorted.append(i)

    if right_index < len(right_array):
        for j in right_array[right_index:]:
            sorted.append(j)

    return sorted

#count -> called at runtime
def findMajority(sortedList):
    # print(sortedList)
    count = 0
    mid = len(sortedList)//2
    maybe = sortedList[mid]

    for i in sortedList:
        if i == maybe:
            count += 1

    if count > mid:
        return 1
    else:
        return -1
    
    

if __name__ == '__main__':
    # input = sys.stdin.read()
    input=input()
    n, *a = list(map(int, input.split()))

    if findMajority(get_majority_element(a, 0, n-1)) == -1:
        print(0)
    else:
        print(1)
