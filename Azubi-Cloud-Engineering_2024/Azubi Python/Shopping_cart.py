#prompt the user to enter the name of theitem and its price, then add it to theshopping_cart list.
name_item = input("Name of item: ")
price_item = input("Price of item: ")
#shopping_cart = []
#list_item = name_item:
shopping_cart = [name_item , price_item]
#shopping_cart.append[name_item, price_item]
print(shopping_cart, {name_item: price_item})
#prompt the user to enter the name of theitem they want to remove, then remove itfrom the shopping_cart list.
item_remove = input("Remove item: ")
shopping_cart.remove(item_remove)
print(shopping_cart)
#loop through the shopping_cart list and print out each item's name and price.
for i in shopping_cart:
    print(i)
#loop through the shopping_cart list and sum up the prices.