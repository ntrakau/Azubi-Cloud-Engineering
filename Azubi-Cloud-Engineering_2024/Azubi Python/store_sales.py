'''
Azubi store has products that customers love. Below are the products, prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products

    -create a new price list that reduces the old prices by $ 5

    -calculate the total revenue generated from the products

    -calculate the average daily revenue generated from the products

    -based on the new prices, which products are less than $ 30 

Below is the data you are to use for the problem :

products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]

prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]
'''

#I got the below code from ChatGPT.I was struggling a bit to solve this one-- however I have learned from this code "stolen code"
# Data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculations
total_price_avg = sum(prices) / len(prices)
new_prices = [price - 5 for price in prices]
total_revenue = sum(price * quantity for price, quantity in zip(prices, last_week))
avg_daily_revenue = total_revenue / 7  # Assuming a week of data

# Products less than $30 based on new prices
affordable_products = [product for product, price in zip(products, new_prices) if price < 30]

# Results
print(f"1. Total price average for all products: ${total_price_avg:.2f}")
print(f"2. New price list reduced by $5: {new_prices}")
print(f"3. Total revenue generated: ${total_revenue}")
print(f"4. Average daily revenue: ${avg_daily_revenue:.2f}")
print(f"5. Products less than $30 based on new prices: {affordable_products}")
