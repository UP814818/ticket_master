SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining".format(tickets_remaining))
    user_name = str(input("What is your name? "))
    try: 
        num_tickets = int(input("{}, how many tickets would you like to purchase? "
            .format(user_name)))
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining"
                .format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please Try again"
            .format(err))
    else:  
        total_due = calculate_price(num_tickets)
        print("Total price due is ${}".format(total_due))
        permission = str(input("Would you like to proceed {}? (Y/N): "
            .format(user_name)))
        while permission != "y" or "n":
            if permission.lower() == "y":
                #TODO: Gather credit card infromation and process it.
                print("SOLD!")
                tickets_remaining -= num_tickets
                break
            elif permission.lower() == "n":
                print("Thank you for your interest {}".format(user_name))
                break
            else:
                print("That's incorrect. Please answer with either y or n")
                permission = str(input("Would you like to proceed {}? (Y/N): "
                .format(user_name)))
print("Sorry the tickets are all sold out!!! :-(")