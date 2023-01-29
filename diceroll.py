import random
while True:
    print("1.Roll the dice? Yes or No")
    choice = (input())
    if choice == 'Yes' or choice == "yes" or choice == 'YES':
        n = random.randint(1, 6)
        if n == 1:
            print("1")
        if n == 2:
            print("2")
        if n == 3:
            print("3")
        if n == 4:
            print("4")
        if n == 5:
            print("5")
        if n == 6:
            print("6")
    else:
        break
