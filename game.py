import random
i=0
for i in range(0,3):
    a=int(input("Enter a number from 1 to 10:"))
    if a==random.randint(1,10):
        print("Winner!!!")
    else:
        print("Try again!!")
print("LOOSER")
