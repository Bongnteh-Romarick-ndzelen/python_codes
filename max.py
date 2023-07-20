Num1 = int (input('Enter the first Number: '))
Num2 = int (input('Enter the second Number: '))
Num3 = int (input('Enter the third Number: '))
#checking the largest number
if Num1>Num2 and Num1>Num3:
    print(f'{Num1} is the largest')
elif Num2>Num1 and Num2>Num3:
    print(f'{Num2} is the largest')
else:
    print(f'{Num3} is the largest')