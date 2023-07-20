class Item:
      def __init__(self, name:str, price:float, quantity:float):
            #Run validation to the reserve arguments
            assert price >= 0
            assert quantity >= 0
            
            #Assign to self
            self.name = name
            self.price = price
            self.quantity = quantity
      def Calculate_total_price(self):
            return self.price * self.quantity
item1 = Item('Phone',100,76)
item2 = Item('Laptop',1000,3)
print(item1.Calculate_total_price())
print(item2.Calculate_total_price())