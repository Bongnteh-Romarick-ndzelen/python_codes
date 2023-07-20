def factorial(n:int):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return "Invalid input "
    return n * factorial(n-1)
n = int(input('Enter a Number: '))
print(factorial(n))
