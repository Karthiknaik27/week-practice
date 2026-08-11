customer_name = input("Enter your name:")
age =  int(input("Enter age: "))
number_of_tickets = int(input("Enter number of tickets:"))
if age < 12:
    ticket_price = 120

elif age >= 12 and age <= 59:
    ticket_price = 200

else:
    ticket_price = 150

total_berfore_discount = ticket_price * number_of_tickets
if number_of_tickets >= 5:
    discount = total_berfore_discount * 10 / 100

else: discount = 0

final_amount = total_berfore_discount - discount

print("/n----- Movie Ticket Booking Summary -----")
print("Customer Name:" , customer_name)
print("Ticket Price: ", ticket_price)
print("Total Before Discount: ", total_berfore_discount)
print("Discount: ", discount)
print("Final Amount: ", final_amount)    
