while True: 
    print("Think of a number between and including 1 & 100")
    remainder3 = int(input("What is the remainder of the number when divided by 3?: "))
    while remainder3 >= 3:
        print("Remainder must be less than 3")
        remainder3 = int(input("What is the remainder of the number when divided by 3?: "))
    while remainder3 < 0:
        print("Remainder must be greater than 0")
        remainder3 = int(input("What is the remainder of the number when divided by 3?: "))
    remainder5 = int(input("What is the remainder of the number when divided by 5?: "))
    while remainder5 >= 5:
        print("Remainder must be less than 5")
        remainder5 = int(input("What is the remainder of the number when divided by 5?: "))
    while remainder5 < 0:
        print("Remainder must be greater than 0")
        remainder3 = int(input("What is the remainder of the number when divided by 5?: "))
    remainder7 = int(input("What is the remainder of the number when divided by 7?: "))
    while remainder7 >= 7:
        print("Remainder must be less than 7")
        remainder7 = int(input("What is the remainder of the number when divided by 7?: "))
    while remainder7 < 0:
        print("Remainder must be greater than 0")
        remainder3 = int(input("What is the remainder of the number when divided by 7?: "))
    for x in range (101):
        if x%3 == remainder3 and x%5 == remainder5 and x%7 == remainder7:
            print("Your number is",x)
    again = input("Do you want to play again?: Y or N: ")
    while again != "Y" and again != "N":
        again = input("Do you want to play again?: Y or N: ")
    if again == "N":
        break