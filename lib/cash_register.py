#!/usr/bin/env python3

class CashRegister:
    pass
    def __init__(self, discount = 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity = 1):
        self.total += price * quantity
        for q in range(quantity):
            self.items.append(item)
        
        cart = {
            "item": item,
            "quantity": quantity,
            "price": price
          }
  
        self.previous_transactions.append(cart)
    
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))

            print(f"After the discount, the total comes to ${self.total}.")

        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "You do not have any previous transactions to void."

        self.total -= (self.previous_transactions[-1]["price"] * self.previous_transactions[-1]["quantity"])
            
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()

        self.previous_transactions.pop()

  
cash_register = CashRegister()
print(cash_register.total)
print(cash_register.discount)
print(cash_register.items)


cash_register_with_discount = CashRegister(20)
print(cash_register.total)
print(cash_register_with_discount.total)
print(cash_register_with_discount.discount)
print(cash_register.items)
print(cash_register_with_discount.items)

cash_register.add_item("bread", 60)
print(cash_register.items)
print(cash_register.total)
print(cash_register_with_discount.discount)
print(cash_register_with_discount.items)

cash_register.add_item("milk", 70, 4)
print(cash_register.items)
print(cash_register.total)
print(cash_register_with_discount.discount)
print(cash_register_with_discount.items)

cash_register_with_discount.add_item("toothpaste", 100, 2)
print(cash_register.items)
print(cash_register.total)
print(cash_register_with_discount.discount)
print(cash_register_with_discount.items)
print(cash_register_with_discount.total)
cash_register_with_discount.apply_discount()
print(cash_register_with_discount.total)
print(cash_register.items)
print(cash_register.total)


cash_register.add_item("eggs", 20, 10)
print(cash_register.items)
print(cash_register.total)
cash_register.void_last_transaction()
print(cash_register.items)
print(cash_register.total)











            
          



   
