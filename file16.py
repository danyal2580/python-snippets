# FOR LOOP

x="Danyal"
for d in x :
    print(d)
#square of a number
for number in range(1,6):
    square=number**2
    print(f"square of {number} is {square}")
#nested for loop
for country in ["pakistan","india","america"]:
   print(country)
   for i in country:
       print(i)
#Range
for q in range(1,21):
    print(q)
#table
for k in range(1,11):
    print("2 x ",k, "=", 2 * k)
print()
#counting vowels
naam="abdullah"
vowels="aeiouAEIOU"
count=0
for m in naam:
    if m in vowels:
        count=count+1
print(count)
print(naam)
  
