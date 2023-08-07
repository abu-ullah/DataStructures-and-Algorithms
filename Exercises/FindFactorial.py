## Given a number, find the factorial
## ex. Factorial(5) == >  5! = 5 x 4 x 3 x 2 x 1

def findFactorialRecursive(number):
    if number == 2:
        return 2
    return number * findFactorialRecursive(number - 1)
    
def findFactorialIterative(number):
    factorial = 1
    while number > 0:
        factorial = factorial * number
        print("Factorial : ", factorial, " || Number : ", number)
        number -= 1
    return factorial

print("Recursive approach: ", findFactorialRecursive(5))

print("Iterative approach: ", findFactorialIterative(5))