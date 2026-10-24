price = float(input("What is the price of the item? $"))
state = input("Enter the destination state: ")
if state == "TX" or state == "LA"
    print("Shipping tax: $1.25")
elif state == "CA":
    print("Shipping tax: $3.25")
else:
    print("Shipping tax: $0.50")
