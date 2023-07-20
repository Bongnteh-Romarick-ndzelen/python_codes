def factorial(n):
    if n == 0 or n ==1:
        return 1
    if n < 0:
        return ("Invalid input")
    return n * factorial(n-1)
n = int(input("Enter a number to find factorial: "))
factorial(n)
print(factorial(n))
if factorial(n) > 100:
    print('You are eligible for the program')
elif factorial(n) == 100:
    print("Welcome to our application\nPlease try again to use our products")
else:
    print('You\'re not eligible to use our platform')