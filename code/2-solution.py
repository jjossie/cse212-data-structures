state_set = set()
print("Actions: ")
print("1: Add State, 2: Remove State, 3: Show All States, 4: Quit")
done = False
while not done:
    user_input = input("Select Action: ")
    try:
        selection = int(user_input)
        if selection == 1:
            state_set.add(input("What state did you visit? "))
        elif selection == 2:
            state_set.remove(input("Enter the state to be removed: "))
        elif selection == 3:
            print(state_set)
        elif selection == 4:
            done = True
            
    except ValueError:
        print("Invalid Input.")