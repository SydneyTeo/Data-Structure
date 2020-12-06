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
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_productfast(input_numbers))
