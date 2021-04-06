stack = []
phrase = input("Enter a word or phrase: ")
for char in phrase:
    stack.append(char)

reversed_phrase = ""
for i in range(0, len(stack)):
    reversed_phrase += stack.pop()

print(reversed_phrase)