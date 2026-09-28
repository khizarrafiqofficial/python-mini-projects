total_sales = 0

for i in range(1, 6):
    sales = float(input(f"Enter sales amount for Employee {i}: Rs. "))
    
    if sales < 50000:
        tax_rate = 0.05
    elif sales <= 100000:
        tax_rate = 0.10
    else:
        tax_rate = 0.15
    
    tax_amount = sales * tax_rate
    
    print(f"Employee {i} -> Sales Amount: Rs. {sales:.2f}, Tax Amount: Rs. {tax_amount:.2f}")
    print("-" * 50)
    
    total_sales += sales

average_sales = total_sales / 5

print(f"\nTotal Sales: Rs. {total_sales:.2f}")
print(f"Average Sales: Rs. {average_sales:.2f}")