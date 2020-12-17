import random

def stresstest(N, M):
    while True:
        n = random.randint(2,N)
        array = []
        for i in range(n):
            array.append(random.randint(0,M))

        result1 = max_pairwise_productslow(array)
        result2 = max_pairwise_productfast(array)

        if result1 == result2:
            print("OK")
        else:
            print(array)
            print(result1, result2)
            print("Error")
            break

def max_pairwise_productslow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_productfast(numbers):
    n = len(numbers)
    max_product = 0
    max_product2 = 0
    max_index = 0
    for i in range(n):
        if numbers[i] > max_product:
            max_index = i
            max_product = numbers[i]

        
    for j in range(n):
        if numbers[j] <= max_product and numbers[j] > max_product2:
            if j != max_index: 
                 max_product2 = numbers[j]

    return (max_product * max_product2)



if __name__ == '__main__':
    stresstest(10,100000)