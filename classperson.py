class Person:
      def __init__(self,name,age):
            self.name = name
            self.age = age
#asking users to input their names
name = input('Enter your Name\n')
age = input('Enter your age\n')
p1 = Person(name, age)
print('My Name is',p1.name)
print('My age is',p1.age)
            