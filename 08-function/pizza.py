# pizza.py

def make_pizza(size,*toppings):
    """概述要制作的比萨"""
    print(f"\nMaking a {size}-innch pizza with the following topping:")
    for topping in toppings:
        print(f"- {topping}")