TICKET_PRICE = 10

tickets_remaining = 100

print("There are {} tickets remaining".format(tickets_remaining))

user_name = str(input("What is your name? "))
num_tickets = int(input("{}, how many tickets would you like to purchase? "
    .format(user_name)))
total_due = num_tickets * TICKET_PRICE
print("Total price due is ${}".format(total_due))
permission = str(input("Would you like to proceed {}? (Y/N): "
    .format(user_name)))
if permission.lower() == "y":
    #TODO: Gather credit card infromatio nand process it.
    print("SOLD!")
    tickets_remaining -= num_tickets
elif permission.lower() == "n":
    print("Thank you for your interest {}".format(user_name))