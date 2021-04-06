done = False
stack = []
while not done:
    string = input("Type something ('undo' to reveal most recent entry, 'q' to quit): ")
    if string == 'undo':
        print(stack.pop())
    elif string == 'q':
        done = True
    else:
        stack.append(string)