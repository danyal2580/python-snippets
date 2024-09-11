# while loop exercise
s1="Python Programming"
l=(len(s1))
x=0
while x<l:
    if s1[x] not in"a,e,i,o,u":
       print(s1[x])
    x=x+1
print("exit")    


x=1
sum=0
while x <=10:
    sum=sum+x
    x=x+1
    
print(sum)

x=1
d=0
while x!="m":
    x=input("enter the value of x or m to exit")
    if x!="m":
       d=d+int(x)
print(d)       

