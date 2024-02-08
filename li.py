from random import randint


def c1():
    """
    Creates a username and password, then asks the user for them
    """
    while True:
        username = input("Create a username: ")
        if username:
            break
        print("A username cannot be blank!")

    while True:
        password = input("Create a password: ")
        if password:
            break
        print("You need a password!")

    while True:
        input_username = input("What is the username: ")
        input_password = input("What is the password: ")
        if username == input_username and password == input_password:
            print("Correct!")
        print("Your details are not correct. Try again!")

def c2():
    """
    Asks the user for a number, then prints all numbers to that number
    """
    while True:
        num = input("Type a number: ")
        try:
            num = int(num)
        except ValueError:
            print("That is not a postive integer! Try again.")
            continue

        if not num >= 0:
            print("That is not a postive integer! Try again.")
            continue
        break

    return_statement = "Numbers: "

    for i in range(0, num + 1):
        if i == num:
            return_statement += f"{i}"
            break
        return_statement += f"{i}, "

    print(return_statement)


def c3():
    print("Type 5 numbers.")

    total = 0

    for i in range(5):
        while True:
            num = input("")
            try:
                num = int(num)
            except ValueError:
                print("That is not an integer! Try again.")
            break

    print(f"The toal is {total}!")


def c4():
    random_number = randint(0, 100)

    for i in range(10):
        while True:
            guessed_number = input("Guess a number: ")
            try:
                guessed_number = int(guessed_number)
            except ValueError:
                print("That is not a number! Please enter a number.")
                continue
            break

        if guessed_number == random_number:
            print(f"You guessed the numbber correctly, after {i + 1} attempts!")
            break
        if i == 10:
            print("You have not guessed the correct number after 10 attempts.")
            print(f"The number is {random_number}.")
            break
        if guessed_number > random_number:
            print("The number I am thinking of is lower.")
        if guessed_number < random_number:
            print("The number I am thinking of is higher.")


def c5():
    """
    Calculator
    """
    print("The calculator")
    while True:
        print("\nWould you like to:")
        print("1) Get asked numbers")
        print("2) Type an equation")
        selection = input("\nSelection: ")
        try:
            selection = int(selection)
        except ValueError:
            print("That is not a number! Try again.")
            continue

        if selection != 1 and selection != 2:
            print("That is not a valid option! Try again.")
            continue

        break

    if selection == 1:
        while True:
            n1 = input("What do you want number 1 to be? ")
            try:
                n1 = int(n1)
            except ValueError:
                print("That is not an integer! Try again.")
                continue
            break

        operations = ["plus", "mines", "times", "divide"]

        while True:
            print("What do you want the operation to be? Choose from: ")
            o1 = input("plus, minus, times, divide, power, or root? ").lower()
            if o1 not in operations:
                print("That is not a valid operation! Try again.")
                continue
            break

        while True:
            n2 = input("What do you want number 2 to be? ")
            try:
                n2 = int(n2)
            except ValueError:
                print("That is not an integer! Try again.")  
                continue
            break

        if o1 == "plus":
            print(f"{n1} {o1} {n2} equals {n1 + n2}")
        if o1 == "minus":
            print(f"{n1} {o1} {n2} equals {n1 - n2}")
        if o1 == "times":
            print(f"{n1} {o1} {n2} equals {n1 * n2}")
        if o1 == "divide":
            print(f"{n1} {o1} {n2} equals {n1 + n2}")
        if o1 == "power":
            print(f"{n1} to the power of {n2} equals {n1 ** n2}")
        if o1 == "root":
            print(f"{n1} to the root of {n2} equals {n1 ** (1/n2)}")

    if selection == 2:

        conditions = [">", "<", "!", "="]
        
        while True:
            try:
                user_input = input("\nType your equation: ")
                if not user_input:
                    raise Exception
                for i in user_input:
                    if i.isalpha():
                        raise Exception
                answer = eval(user_input)
            except Exception:
                print("This equation is invalid! Try again.")
                continue

            has_conditions = False

            for char in user_input:
                if char in conditions:
                    has_conditions = True
                    break

            if not has_conditions:
                print(f"{user_input} equals {answer}")
            else:
                print(f"The equation {user_input} is {answer}")



def c6v1():

    score = 0

    print("Math test")

    for i in range(10):
        operation = randint(0, 3)
        operations = ["+", "-", "*", "/"]
        
        n1 = 1
        n2 = 1
        
        if operation == 0:
            n1 = randint(1, 100)
            n2 = randint(1, 100)

        if operation == 1:
            n1 = randint(1, 100)
            n2 = randint(1, n1)

        if operation == 2:
            n1 = randint(1, 12)
            n2 = randint(1, 12)

        if operation == 3:
            while True:
                n1 = randint(1, 144)
                n2 = randint(1, 12)
                if n1 % n2 == 0:
                    break

        while True:
            print()
            response = input(f"What is {n1} {operations[operation]} {n2}? ")
            answer = int(eval(f"{n1}{operations[operation]}{n2}"))
            try:
                response = int(response)
            except ValueError:
                print("That is not a number! Try again.")
                continue
            if response == answer:
                print("The answer was correct!")
                score += 1
                break

            print(f"{n1} {operations[operation]} {n2} does not equal {response}.")
            print(f"The answer is {answer}.")
            break

    passfail = "passed" if score == 10 else "failed"
    print(f"\nYou answered {score} questions correctly. You {passfail} the test!")

c5()

# while True:
#     selection = input("What program do you want to run? (1-6) ")
#     try:
#         selection = int(selection)
#     except ValueError:
#         print("Please select a valid option!")
#         continue

#     break
