"""This implemenation creates a ternary search tree. Similar to a binary
search tree, except each node can have up to three children. The center 
node allows for duplicates to be added to the tree without consequences, 
except for the possibility of a long list of duplicates, which would 
create an unbalanced and inefficient tree. 
"""

class Node:
    def __init__(self, data):
        self.left = None
        self.center = None
        self.right = None
        self.data = data

def insert(root, node):
    if root.data == node.data:
        if root.center is None:
            root.center = node
        else:
            insert(root.center, node)
    elif node.data > root.data:
        if root.right is None:
            root.right = node1
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


def main():
    print("1: Add First Name, 2: Check for First Name, 3: Quit")
    root_name = None
    done = False
    while not done:
        user_input = input("Select Action: ")
        try:
            selection = int(user_input)
            if selection == 1:
                if root_name is None:
                    root_name = Node(input("Enter a name: "))
                else:
                    insert(root_name, Node(input("Enter a name: ")))
            elif selection == 2:
                if root_name is None:
                    print("Tree is empty.")
                else:
                    num = input("Enter a name: ")
                    print(f"{num} is in the tree: {contains(root_name, num)}")
            elif selection == 3: 
                done = True
        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":    
    main()