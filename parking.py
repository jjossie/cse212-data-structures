parking_lot = set()
print("Actions: ")
print("1: Park Car, 2: Remove Car, 3: Show parking lot, 4: Quit")
done = False
while not done:
    user_input = input("Select Action: ")
    try:
        selection = int(user_input)
        if selection == 1:
            parking_lot.add(input("Enter the license plate number of the car being parked: "))
        elif selection == 2:
            parking_lot.remove(input("Enter the license plate number of the car to be removed: "))
        elif selection == 3:
            print(parking_lot)
        elif selection == 4:
            done = True
            
    except ValueError:
        print("Invalid Input.")

