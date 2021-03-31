val1 = "One"
val2 = "Two"
val3 = "Three"
val4 = "Four"


print(hash(val1))
print(hash(val2))
print(hash(val3))
print(hash(val4))

sample_set = set()

sample_set.add(val1)
sample_set.add(val2)
sample_set.add(val3)
sample_set.add(val4)

sample_set.add(10)
sample_set.remove("Four")



if 10 in sample_set:
    print("10 is in the set!") # This will print
print(sample_set)

