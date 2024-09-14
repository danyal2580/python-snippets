#Tuple
Fruit_names = ("Apples", "Banana", "Mango", "Grapes")
print(Fruit_names[3])

# Tuple constructor
marks_list = [120, 220, 330, 440, 550]
marks_tuple = tuple(marks_list)
print(marks_tuple)


# Check if an element is not in the tuple
print("orange" not in Fruit_names)

# Tuples do not support item assignment (unlike lists)
# To modify a tuple, you need to convert it to a list first
Fruit_names_list = list(Fruit_names)
Fruit_names_list.remove("Banana")
Fruit_names_list.pop(0)
Fruit_names_list.append("cherry")
Fruit_names_list.insert(1, "strawberry")
Fruit_names_list[2] = "orange"

# Convert back to tuple
Fruit_names = tuple(Fruit_names_list)
print(Fruit_names)


# Looping through a tuple
Fruit_names = ("Apples", "Banana", "Mango", "Grapes")
for x in Fruit_names:
    print(x)

# Tuple multiplication
multiply_Fruit_names = Fruit_names * 2
print(multiply_Fruit_names)

# Tuple of weekdays
weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri")

# Slicing Examples
print(weekdays[1:3]) 
print(weekdays[1:])  
print(weekdays[:4])  
print(type(weekdays))