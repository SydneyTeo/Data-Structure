#BAE WE DID IT!!
#BAE WE DID IT!!
#BAE WE DID IT!!
#BAE WE DID IT!!
#BAE WE DID IT!!

import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    num = []
    op = []
    for i in dataset:
        if i.isdigit() == True:
            num.append(int(i))
        else:
            op.append(i)
    
    #maxtable
    maxvalues = [[None for i in range(len(num))] for j in range(len(num))]
    #mintable
    minvalues = [[None for i in range(len(num))] for j in range(len(num))]

    for ii in range(len(num)):
        minvalues[ii][ii] = num[ii]
        maxvalues[ii][ii] = num[ii]

    #Here is the weird ass way to iterate over a diagonal table.
    for j in range(1,len(num)):
        for i in range(len(num)-j):
            minvalues[i][i+j], maxvalues[i][i+j] = minMax(i,i+j,op,minvalues,maxvalues)
    return maxvalues[0][len(num)-1]

def minMax(i,j,op,minvalues,maxvalues):
    minNum = math.inf
    maxNum = -math.inf

    for k in range(i,j):
        a = evalt(maxvalues[i][k],maxvalues[k+1][j],op[k])
        b = evalt(maxvalues[i][k],minvalues[k+1][j],op[k])
        c = evalt(minvalues[i][k],maxvalues[k+1][j],op[k])
        d = evalt(minvalues[i][k],minvalues[k+1][j],op[k])
        minNum = min(minNum, a, b, c, d)
        maxNum = max(maxNum, a, b, c, d)
        
    return minNum,maxNum

if __name__ == "__main__":
    print(get_maximum_value(input()))
