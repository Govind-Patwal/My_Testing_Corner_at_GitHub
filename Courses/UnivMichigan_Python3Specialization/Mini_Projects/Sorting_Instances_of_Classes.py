class Fruit():
    def __init__ (self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__ (self):
        return '{} is priced as {} and has a quanity of {} in stock'.format(self.name, self.price, self.quantity)

fruit_names = ['Apples', 'Pears', 'Bananas', 'Grapes']        
fruit_prices = [12,45,1,3]
fruit_qty = [100,34,789,12]

fruit_tuples = zip(fruit_names, fruit_prices, fruit_qty)

fruit_instance_list = [Fruit(n,p,q) for n,p,q in fruit_tuples ]

sorted_fruits_on_name = sorted(fruit_instance_list, key = lambda self: self.name)
sorted_fruits_on_price = sorted(fruit_instance_list, key = lambda self: self.price)
sorted_fruits_on_qty = sorted(fruit_instance_list, key = lambda self: self.quantity)

print('\n*** sorting instances based on names ***')
print( [instance.name  for instance in sorted_fruits_on_name ] )
print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_name ] )

print('\n*** sorting instances based on prices ***')
print( [instance.price  for instance in sorted_fruits_on_price ] )
print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_price ] ) 

print('\n*** sorting instances based on Quantity ***')
print( [instance.quantity  for instance in sorted_fruits_on_qty ] )
print( [ (instance.name, instance.price, instance.quantity)  for instance in sorted_fruits_on_qty ] ) 
