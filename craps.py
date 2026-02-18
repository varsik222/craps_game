import random

def main():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    summ = x + y
    
    return x, y, summ

x, y, summ = main()

print(f"the summ of dice is: {x} + {y}: ", summ)

#You could write this in a more Pythonic way for readability
#Its shorter and easier to read
if summ in (7, 11):
    print("You won!")

#Same here
elif summ in (2, 3, 12):
    print("Craps the casino wins!!!")
else:
    target = summ
    print(f"Now your goal is {target}")
    
    while True:
        x, y, summ = main()
        print(f"The sum of dice is: {x} + {y} = {summ}")

        if summ == target:
            print("You won!")
            break
        elif summ == 7:
            print("You lose!")
            break
