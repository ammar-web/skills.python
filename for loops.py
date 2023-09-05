### USING "FOR LOOPS" IN PYTHON ###

### CREATING A PURCHASE BILL USING PYTHON ###


prices = [10, 20, 30, 100]

total = 0

for price in prices:
    
    total += price

print(f"total_payment:{total}")

total_payment = total

if total_payment > 200:
    
    print("Oops it's out of my budget!!")

if total_payment < 200:
    
    print("thank you")
