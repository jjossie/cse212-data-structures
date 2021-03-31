class car:
    # cars = []
    def __init__(self, color, style):
        self.color = color
        self.style = style
        # car.cars.append(self)
    def __str__(self):
        return f""

def createCar():
    color = input("What color? ")
    style = input("What body style? ")
    return car(color, style)


class lot:
    def __init__(self):
        self.spaces = set()
    def park(self, car):
        self.spaces.add(car)
    def leave(self, car):
        self.spaces.remove(car)
    def isParked(self, car):
        return car in self.spaces
    def __str__(self):
        lot_string = ""
        for space in self.spaces:
            lot_string.append(f"space {space}")
        return self.spaces

def main():


    main_lot = lot()
    print("Actions ('q' to quit):")
    print("1: Create Car, 2: Park Car, 3: Remove Car, 4: Show parking lot")
    actions = {2: main_lot.park, 3: main_lot.leave}

    done = False
    while not done:
        
        raw_input = input("Select Action: ")
        # this_car = None
        if raw_input == 'q':
            done = True
        else:
            try:
                selection = int(raw_input)
                if selection == 1:
                    color = input("What color? ")
                    style = input("What body style? ")
                    this_car = car(color, style)
                elif selection == 4:
                    print(main_lot)
                else:
                    print(f"\n\n\n-------\n\n\nexecuting {selection} on {str(this_car)}\n\n\n-----\n\n\n")
                    actions[selection](this_car)
                    
            except ValueError:
                print("Invalid Input.")



if __name__ == "__main__":
    main()