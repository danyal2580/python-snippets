membership=input("enter any membership[gold,silver,bronze,none] :")
if membership not in ["gold","silver","bronze","none"]:
     print("invalid membership")
elif membership=="gold":
     print("25% discount")
elif membership=="silver":
     print("15% discount")
elif membership=="bronze":
     print("10% discount")
elif membership=="none":
     print("Standard pricing")

number=int(input(("please enter the number")))
if number>0:
    print("positive number")
elif number<0:
    print("negative number")
elif number==0:
    print("0 number")
