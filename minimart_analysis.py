#simulate new orders in a minimart
orders = [
    {"customer": "lateef", "product": "shoe", "qty": 3, "price": 9.5},
    {"customer": "mariam", "product": "pen", "qty": 10, "price": 3.0},
]

#identify large orders
for order in orders:
    if order["qty"] > 5 or order["price"] * order["qty"] > 25:
        print(f"Large order: {order['customer']}") 
    else:
        print(f"Regular order: {order['customer']}") 


#apply type conversion and discounts
for order in orders:
    order["price"] = float(order["price"])
    if order["qty"] >= 10:
        order["price"] *= 0.9  
    elif order["qty"] >= 5:
        order["price"] *= 0.95
    else:
        order["price"] *= 1.0

#Generate summary report
report = {}
report["total_products_sold"] = sum(order["qty"] for o in orders)
report["most_popular_product"] = max(orders, key=lambda x: x["qty"])["product"]


revenue_per_customer = {}

for order in orders:
    customer = order["customer"]      
    quantity = order["qty"]            
    price = order["price"]             

    revenue_for_this_order = quantity * price

    if customer in revenue_per_customer:
        revenue_per_customer[customer] += revenue_for_this_order
    else:
        revenue_per_customer[customer] = revenue_for_this_order

report["revenue_per_customer"] = revenue_per_customer
print(report)

