
# home task build a calculator
x=int(input("enter no 1 "))
y=int(input("enter no 2 "))
z=input("Enter any operator[+,-,*,/]")
if z== "+":
   print(f"Addition {x+y}")

elif z== "-":
   print(f"subtraction {x-y}")

elif z== "*":
   print(f"Multiplication {x*y}")

elif z== "/":
     if y==0:
        print("Error:division with zero is not allowed")
     
else:
  print("end")   