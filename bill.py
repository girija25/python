name=str(input("Enter your name:"))
fromloc=str(input("Enter your from location:"))
toloc=str(input("Enter your destination:"))
dis=int(input("Enter distance in kilometres:"))
print("1.premium")
print("2.non-premium")
print("3.ac")
print("4.non-ac")
print("5.sleeper")
print("6.semi-sleeper")
category=int(input("selct the category"))

if category==1:
    cost=dis*5
elif category==2:
    cost=dis*3.50
elif category==3:
    cost=dis*4
elif category==4:
    cost=dis*2
elif category==5:
    cost=dis*2.50
elif category==6:
    cost=dis*1.50
else:
    print("invalid selection")
print("--------YOUR BILL-------")
print("NAME:        ",name)
print("FROM:        ",fromloc)
print("DESTINATION:     ",toloc)
print("DISTANCE:        ",dis)
print("COST:        ",cost)
