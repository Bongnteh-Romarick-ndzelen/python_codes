class Student:
      def __init__(self, name, age, gender, quantity, price):
            self.name = name
            self.age = age
            self.gender = gender
            self.quantity = quantity
            self.price = price
      def Calculate_total_price(self):
            return self.price * self.quantity
#creating an object
Y1 = Student('Romarick',18,'male',4,2500)
print(Y1.name,'You are a',Y1.gender)
print('Your age is',Y1.age)
print('You have cosume a quantity of',Y1.quantity,
      '\nand your total price is')
print(Y1.Calculate_total_price())
print(Y1.__dict__)
print(Y1.__doc__)
            
     