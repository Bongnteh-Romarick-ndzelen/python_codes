n = int(input("Enter n to find factorial: "))
def factorial(n):
    if n<=1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(n))
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num//2)
    else:
        print('\nYou Entered a negative number.\nPlease enter a positive number!')
    print(num%2,end='')
number = int(input("Enter any decimal number: "))
decimalToBinary(number)