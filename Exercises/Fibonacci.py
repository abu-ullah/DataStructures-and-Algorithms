## Pattern: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...add()
## Each value is the sum of the 2 previous values

## Function recieves index, returns the value of the index
def fibonacciIterative(num):
    sequence = [0, 1]
    for i in range(2, num + 1):
        newValue = sequence[i - 1] + sequence[i - 2]
        sequence.append(newValue)
    return sequence[num]
        
def fibonacciRecursive(num): 
    if num < 2:
        return num
    return fibonacciRecursive(num - 1) + fibonacciRecursive(num - 2)

print('Iterative : ', fibonacciIterative(8))

print('Recursive: ', fibonacciRecursive(8))