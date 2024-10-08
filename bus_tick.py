#Write a program that simulates a bus ticket booking system.
# The bus has 8 seats. Each time a seat is booked, the available seats decrease.
# When there are no seats left, the loop stops and displays a
# message saying "All seats are booked."


available_ticket = 10

is_avaiable = True
continue_booking = True

while is_avaiable:
    if continue_booking:
        book_ticket = int(input("Enter number of tickets to be booked/ click 1 to exit"))

    if book_ticket == 1:
        print("You logged off")
        break

    if (available_ticket > 0) and (book_ticket <= available_ticket):
        print(f"Your {book_ticket} seats are booked...Thanks for booking")
        available_ticket -= book_ticket
        continue
    elif book_ticket > available_ticket and available_ticket !=0:
        print(f"{book_ticket} Tickets marked for booking is greater than available ticket: {available_ticket}...kindly re book")
        continue
    else:
        print("All Tickets booked")
        break



