#!/usr/bin/env python3
# Production application

def calculate_price(amount):
    tax = 0.20
    return amount * (1 + tax)

if __name__ == "__main__":
    print(f"Price with tax: ${calculate_price(100)}")
