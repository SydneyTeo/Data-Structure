# Uses python3
import sys
import math



def optimal_sequence(n):
    sequence = []
    num_op = [0,0]

    for i in range (2, n+1):
        temp1, temp2, temp3 = [math.inf] * 3
        num_op.append(math.inf)
        
        if i%2 == 0:
            temp1 = num_op[i//2] + 1
        if i%3 == 0:
            temp2 = num_op[i//3] + 1
        temp3 = num_op[i-1] + 1

        num_op[i] = min(temp1, temp2, temp3)
    

    nums = [n]
    while n != 1:
        if  n%3 == 0 and num_op[n]-1==num_op[n//3]:
            nums+=[n//3]
            n = n//3
            sequence.append(n)
            
        elif  n%2 == 0 and num_op[n]-1==num_op[n//2]:
            nums+=[n//2]
            n = n//2
            sequence.append(n)
        else: 
            nums += [n-1]
            n=n-1
            sequence.append(n)

    return reversed(sequence)

 
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence))
for x in sequence:
    print(x, end=' ')
print(n)
