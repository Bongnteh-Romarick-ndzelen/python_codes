import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = (b**2)-(4*a*c)
if d==0:
      print("One real root:")

      print((-b+(d**0.5))/(2*a))
elif d>0:
      print("two roots: ")
      root1 = (-b+(d**0.5))/(2*a)
      root2 = (-b-(d**0.5))/(2*a)
      print("root1= "+str(root1))
      print("root2= "+str(root2))
else:
      print("Two roots are imaginary: ")