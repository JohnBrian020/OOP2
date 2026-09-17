products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Headphones", "price": 150},
    {"name": "Tablet", "price": 500}
]

def filter_products(products, condition):
    result = []
    
    for product in products:
        if condition(product):
            result.append(product)        
    return result

#Callback version
def expensive_product(product):
    return product["price"] > 700

def cheap_product(product):
    return product["price"] < 500

#Use callbacks
expensive = filter_products(products, expensive_product)
cheap = filter_products(products, cheap_product)

print("Expensive:", expensive)
print("Cheap:", cheap)