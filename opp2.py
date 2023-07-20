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
name = input('Enter the name of the Item: ')
price = float(input('Enter the price of the item: '))
quantity = float(input('Enter the quantity of the Item: '))
item = Item(name, price, quantity)
print(item.Calculate_total_price())