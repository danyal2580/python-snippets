#nested while loop

i=1
while i<=5:
     j=1
     while j<=5:
        print(j, end=" ")
        j=j+1
     print()
     i=i+1

i=1
while i<=5:
     j=1
     while j<=i:
        print(j, end=" ")
        j=j+1
     print()
     i=i+1

i=1
while i<=5:
     j=1
     while j<=i:
        print("*", end=" ")
        j=j+1
     print()
     i=i+1

i=1
while i<=5:
     print("* "*i)
     i=i+1