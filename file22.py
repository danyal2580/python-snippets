# Dictionary
Fruit_colors = {"Apple": "Red", "Banana": "Yellow", "Mango": "Orange", "Grapes": "Green"}
print(Fruit_colors["Grapes"])  #key:value pair

# Using the dict constructor to create a dictionary from a list of tuples
marks = dict([(1, 120), (2, 220), (3, 330), (4, 440), (5, 550)])  
print(marks)

# Checking if a key exists in the dictionary
print("Mango" in Fruit_colors)

# Removing an item from the dictionary
Fruit_colors.pop("Banana")

# Adding or updating items in the dictionary
Fruit_colors["Cherry"] = "Red"
Fruit_colors["Strawberry"] = "Red"
Fruit_colors["Orange"] = "Orange"
print(Fruit_colors)

# Looping through a dictionary (keys and values)
Fruit_colors = {"Apple": "Red", "Banana": "Yellow", "Mango": "Orange", "Grapes": "Green"}
for key, value in Fruit_colors.items():
    print(f"{key}: {value}")

# Original list of numbers
numbers = [20, 50, 68, 89, 100, 119, 34, 8, 19]

# Dictionary comprehension 
numbers = [20, 50, 68, 89, 100, 119, 34, 8, 19]
even_dict = {}
for num in numbers:
    if num % 2 == 0:
        even_dict[num] = num  

print(even_dict)
