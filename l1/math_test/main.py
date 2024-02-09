from questions import MathTestConstructor
from time import time


test_constructor = MathTestConstructor()
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
        test_level = test_constructor.difficulty
        test_method = getattr(test_constructor, f"test_{test_level}")
        test_start = time()
        test_score = test_method()
        test_end = time()

        print(f"\nYou scored {test_score} in the level {test_level} test.\n")
        if test_score >= 8 and test_level < 5:
            print(f"You passed level {test_level}!")
            print(f"You can now move onto {test_level + 1}!")
            test_constructor.difficulty += 1
        if test_score >= 8 and test_level == 5:
            print(f"You have passed level {test_level}!")
            print("⚠️  You have reached the maximum level.")
            if test_end - test_start > 30:
                print("However, you clearly need more practising!")
                print("Try test 5 again, but aim to complete it quicker.")
                print(test_end - test_start)
            else:
                print("Congrats on beating the game (:")
        if 5 <= test_score < 8:
            print(f"You barely passed level {test_level}!")
            print("However, you can do better! Try the test again.")
        if test_score < 5:
            print(f"You failed level {test_level}")
            print("How about you go down a level to refine your skills a bit?")
            test_constructor.difficulty -= 1

    if selection == 2:
        exit()
