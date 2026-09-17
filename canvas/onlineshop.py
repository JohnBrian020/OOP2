orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Phone", "price": 800},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 900},
    {"product": "Monitor", "price": 500}
]

def process_orders(orders, action):
    for order in orders:
        action(order)
        
#Callback functions
def print_order(order):
    print(f"Order: {order['product']} - ${order['price']}")
    
