#Break statement
numbers = [1, 2, 3, 7, 5, 6]

for num in numbers:
    if num == 7:
        print("Number 7 found! Breaking the loop.")
        break
    print(f"Current number: {num}")

#continue
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")
