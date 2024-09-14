# Set 
Fruit_names = {"Apples", "Banana", "Mango", "Grapes"}
print("Grapes" in Fruit_names)  
# Using the set constructor to create a set from a list of numbers
marks = set([120, 220, 330, 440, 550])  
print(marks)

# Checking for an element in the set
print("orange" in Fruit_names)


# Removing an item from the set
Fruit_names.remove("Banana")

# Adding items sets don’t have append, instead, use add)
Fruit_names.add("cherry")
Fruit_names.add("strawberry")
Fruit_names.add("orange")
print(Fruit_names)

# Looping through a set
Fruit_names = {"Apples", "Banana", "Mango", "Grapes"}
for x in Fruit_names:
    print(x)
# Original list of numbers
numbers = [20, 50, 68, 89, 100, 119, 34, 8, 19]

# Set comprehension to get only even numbers
even_set = set()
for num in numbers:
    if num % 2 == 0:
        even_set.add(num)

print(even_set)
