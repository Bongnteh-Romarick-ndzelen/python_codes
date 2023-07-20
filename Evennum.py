start = int(input("Enter the starting Number: "))
end = int(input("Enter the ending Number: "))

for i in range(start,end):
    
    #checking whether a number is even or not
    if i%2 == 0:
        print(i)
