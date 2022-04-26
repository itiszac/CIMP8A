#! /usr/bin/env python3

from decimal import Decimal

order_total = Decimal("100.05")
discount_percent = Decimal(".1")
discount = order_total * discount_percent

subtotal = order_total - discount
tax_percent = Decimal(".08")
sales_tax = subtotal * tax_percent
invoice_total = subtotal + sales_tax

print("{:15} {:>10.2f}".format("Order Total:", order_total))
print("{:15} {:>10.2f}".format("Discount:", discount))
print("{:15} {:>10.2f}".format("Subtotal:", subtotal))
print("{:15} {:>10.2f}".format("Sales Tax:", sales_tax))
print("{:15} {:>10.2f}".format("Invoice Total:", invoice_total))
