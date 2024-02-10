from questions import MathTestConstructor
from time import time


test = MathTestConstructor()
print("Welcome to the math test hub!")

while True:
    print("\nWhat do you want to do?\n")
    selection = input("1) Start\n2) Quit\n")
    try:
        selection = int(selection)
    except ValueError:
        print("Invalid selection! Please type a number.")
        continue

    if selection == 1:
        test_start = time()
        test.test()
        test_end = time()
        test_time = test_end - test_start

        print(f"""
\nYou got {test.score} our of 10 correct on the level {test.difficulty} maths test.""")
        print(f"\nYou completed the test in {int(test_end - test_start)} seconds!")

        if test.score >= 8:
            print(f"You have passed level {test.difficulty}!")
            if test_time <= 30:
                print("You can now proceed to the next level.")
                if test.difficulty == 5:
                    print("⚠️ You have reached the maximum level. Congrats.")
                else:
                    test.difficulty += 1
            else:
                print("However, you were too slow. Be faster.")

        elif 5 <= test.score < 8:
            print(f"You have barely passed level {test.difficulty}!")
            print("However, you have bad accuracy. Try the test again.")

        elif test.score < 5:
            print(f"You  have failed level {test.difficulty}")
            print("How about you go down a level to refine your skills a lil bit?")
            test.difficulty -= 1

    if selection == 2:
        exit()
