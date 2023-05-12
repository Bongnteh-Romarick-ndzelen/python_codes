class Item:
      pay_rate = 0.9 #The pay rate after 20% discount
      def __init__(self, name:str, price:float, quantity:float):
            #Run validation to the reserve arguments
            assert price >= 0, f'Price {price} is not greater than or equal to zero'
            assert quantity >= 0, f'Quantity {quantity} is not greater than or equal to zero'
            
            #Assign to self
            self.name = name
            self.price = price
            self.quantity = quantity
      def Calculate_total_price(self):
            return self.price * self.quantity
item1 = Item('Phone',100,76)
item2 = Item('Laptop',1000,86)
print(item1.Calculate_total_price())
print(item2.Calculate_total_price())
print(Item.__dict__)
print(item1.__dict__)