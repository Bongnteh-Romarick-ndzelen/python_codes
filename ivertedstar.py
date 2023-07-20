n = int ( input("Enter an interger: "))
print("Factors are: ")
i = 1
while(i<=n):
    k=0
    if(n%i==0):
        j=1
        while(j<=1):
            if(i%j==0):
                k+=1
            j+=1
        if(k==2):
            print(i)
    i+=1
