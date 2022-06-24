#fibonnaci 

# states that fibonnaci of a number n is the sum of f(n-1) + f(n-2)
#f(0) =0
#f(1) = 1
#f(2) = f(0) + f(1) = 1
#f(3) = f(1) + f(2) = 2
#f(4) = f(3) + f(2) = 3

def fibonacci(num):

    if num == 0:

        return 0

    elif num == 1:

        return 1

    else:

        return fibonacci(num - 1) + fibonacci(num -2)

number = int(input('Find fibonacci of ? '))

print(fibonacci(number))