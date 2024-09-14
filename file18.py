#list
Furit_names=["Apples","Banana","Mango","Graphes"]
print(Furit_names[3])
marks=list((120,220,330,440,550)) #constructor
print(marks)
print("orange" not in Furit_names)
print(Furit_names)
Furit_names.remove("Banana")
Furit_names.pop(0)
Furit_names.append("cherry")
Furit_names.insert(1,"strawberry")
Furit_names[2]="orange"
print(Furit_names)
country= "Pakistan"
print(country[5])
print(country[2:])
print(country[1:5])
print("P" in country)
print(country.upper())
print(country.replace("Pakistan","Pakistan zindabad"))
print()

#looping through a list
Furit_names=["Apples","Banana","Mango","Graphes"]
for x in Furit_names:
    print(x)
    
#list multiplication
multiply_Furit_names=Furit_names*2
print(multiply_Furit_names)

#list comprehension
numbers = [20, 50, 68, 89, 100, 119, 34, 8, 19]
even_list=[]
for num in numbers:
    if num%2==0:
       even_list.append(num)
print(even_list)


