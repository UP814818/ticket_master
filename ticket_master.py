TICKET_PRICE = 10

tickets_remaining = 100

print("There are {} tickets remaining".format(tickets_remaining))

user_name = str(input("What is your name? "))
num_tickets = int(input("{}, how many tickets would you like to purchase? "
    .format(user_name)))
total_due = num_tickets * TICKET_PRICE
print("Total price due is ${}".format(total_due))