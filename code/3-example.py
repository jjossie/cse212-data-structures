class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, node):
    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    elif node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def contains(root, data):
    if root.data == data:
        return True
    elif data < root.data:
        if root.left is None:
            return False
        else:
            return contains(root.left, data)
    elif data > root.data:
        if root.right is None:
            return False
        else:
            return contains(root.right, data)

def get_number():
    valid = False
    while not valid:
        try:
            user_input = int(input("Enter a Phone Number: "))
            if len(str(user_input)) == 10 and user_input >= 0:
                valid = True
            else:
                print("Not a valid phone number.")
        except ValueError:
            print("Please enter only numbers.")
    return user_input

def main():
    print("1: Add Phone Number, 2: Check for Phone Number, 3: Quit")
    root_number = None
    done = False
    while not done:
        user_input = input("Select Action: ")
        try:
            selection = int(user_input)
            if selection == 1:
                if root_number is None:
                    root_number = Node(get_number())
                else:
                    insert(root_number, Node(get_number()))
            elif selection == 2:
                if root_number is None:
                    print("Tree is empty.")
                else:
                    num = get_number()
                    print(f"{num} is in the tree: {contains(root_number, num)}")
            elif selection == 3: 
                done = True
        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":    
    main()