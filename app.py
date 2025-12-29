#!/usr/bin/env python3
# Production application

def calculate_price(amount, discount=0):
    tax = 0.20
    discounted = amount * (1 - discount)
    return discounted * (1 + tax)

if __name__ == "__main__":
    print(f"Price with tax: ${calculate_price(100)}")
    print(f"Price with 10% discount: ${calculate_price(100, 0.10)}")
