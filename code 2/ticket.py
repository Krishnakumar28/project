def print_tickets():
    """Print the tickets of the user."""
    for user_name, seats in user_tickets.items():
        print(f"\nYou, {user_name.title()}, have chosen {len(seats)} seat(s).")
        for seat in seats:
            print(f"\tSeat number: {seat}")


user_tickets = {}
print("WELCOME TO KRISHNA TRAVELS")
available_seats = ['1a', '2a', '19b', '20d', '21e', '13g', '15f', '14f', '13a', '12g' ]


start_prompt = "\nWould you like to start booking your ticket? (yes/no) "
wanted_seats_prompt = "\nHow many seats are you booking today?"
wanted_seats_prompt += "\nEnter the number: "
name_prompt = "What is your name? "
seat_prompt = "\nPlease enter the number of the seat you would like to book: "
go_again_prompt = "Would you like to let someone else book their tickets? (yes/no) "



print("Welcome To The Seat Booking Portal!")

start = input(start_prompt)
if start.lower() == 'yes':
    while True:
        seats = []

        
        wanted_seats = input(wanted_seats_prompt)
        
        wanted_seats = int(wanted_seats)
        
        if wanted_seats > len(available_seats):
            print(f"\n--I'm sorry, we only have {len(available_seats)} "
                "seats available--")
            print("--Please try again--")
            continue

        
        user_name = input(name_prompt)

        
        while True:

           
            print("\nHere are the available seats:")
            for seat in available_seats:
                print(seat)

           
            seat = input(seat_prompt)

            
            if seat in available_seats:
                available_seats.remove(seat)
            
            else:
                print("\n--I'm sorry you have chosen an invalid seat--"
                    "\n-Please try again-")
                continue

           
           
            seats.append(seat)

           
            if wanted_seats > 1:
                print("\nYou can now choose another seat.")
              
                wanted_seats-=1
                continue
            else:
                break

       
        user_tickets[user_name] = seats

       
        if available_seats:
            go_again = input(go_again_prompt)
            if go_again == 'no':
                break
        else:
            break

    print_tickets()
    print("\nWe will now redirect you to the payment portal."
        "\nThank You for choosing us.")

else:
    print("You can always come by later!")