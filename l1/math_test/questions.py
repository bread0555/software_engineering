from random import randint


class MathTestConstructor:
    def __init__(self):
        self.difficulty = 3
        self.operations = ["+", "-", "*", "/", "**", "**"]

    def test_1(self):

        score = 0

        for i in range(10):
            operation = randint(0, 1)

            n1 = 1
            n2 = 1

            if operation == 0:
                n1 = randint(1, 10)
                n2 = randint(1, 10)

            if operation == 1:
                n1 = randint(1, 10)
                n2 = randint(1, n1)

            while True:
                print()
                response = input(f"What is {n1} {self.operations[operation]} {n2}? ")
                answer = int(eval(f"{n1}{self.operations[operation]}{n2}"))
                try:
                    response = int(response)
                except ValueError:
                    print("That is not a number! Try again.")
                    continue
                if response == answer:
                    print("The answer was correct!")
                    score += 1
                    break

                print(f"{n1} {self.operations[operation]} {n2} does not equal {response}.")
                print(f"The answer is {answer}.")
                break

        return score


    def test_2(self):

        score = 0

        for i in range(10):
            operation = randint(0, 3)

            n1 = 1
            n2 = 1

            if operation == 0:
                n1 = randint(1, 50)
                n2 = randint(1, 50)

            if operation == 1:
                n1 = randint(1, 50)
                n2 = randint(1, n1)

            if operation == 2:
                n1 = randint(1, 12)
                n2 = randint(1, 5)

            if operation == 3:
                while True:
                    n1 = randint(1, 60)
                    n2 = randint(1, 12)
                    if n1 % n2 == 0:
                        break

            while True:
                print()
                response = input(f"What is {n1} {self.operations[operation]} {n2}? ")
                answer = int(eval(f"{n1}{self.operations[operation]}{n2}"))
                try:
                    response = int(response)
                except ValueError:
                    print("That is not a number! Try again.")
                    continue
                if response == answer:
                    print("The answer was correct!")
                    score += 1
                    break

                print(f"{n1} {self.operations[operation]} {n2} does not equal {response}.")
                print(f"The answer is {answer}.")
                break

        return score


    def test_3(self):

        score = 0

        for i in range(10):
            operation = randint(0, 3)

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
                response = input(f"What is {n1} {self.operations[operation]} {n2}? ")
                answer = int(eval(f"{n1}{self.operations[operation]}{n2}"))
                try:
                    response = int(response)
                except ValueError:
                    print("That is not a number! Try again.")
                    continue
                if response == answer:
                    print("The answer was correct!")
                    score += 1
                    break

                print(f"{n1} {self.operations[operation]} {n2} does not equal {response}.")
                print(f"The answer is {answer}.")
                break

        return score


    def test_4(self):

        score = 0

        for i in range(10):
            operation = randint(0, 5)

            n1 = 1
            n2 = 1

            if operation == 0:
                n1 = randint(1, 500)
                n2 = randint(1, 500)

            if operation == 1:
                n1 = randint(1, 500)
                n2 = randint(1, n1)

            if operation == 2:
                n1 = randint(1, 15)
                n2 = randint(1, 15)

            if operation == 3:
                while True:
                    n1 = randint(1, 225)
                    n2 = randint(1, 15)
                    if n1 % n2 == 0:
                        break

            if operation == 4:
                n1 = randint(1, 12)
                n2 = 2

            if operation == 5:
                n1 = randint(1, 12)
                n2 = 1/2

            while True:
                print()
                response = input(f"What is {n1} {self.operations[operation]} {n2}? ")
                answer = int(eval(f"{n1}{self.operations[operation]}{n2}"))
                try:
                    response = int(response)
                except ValueError:
                    print("That is not a number! Try again.")
                    continue
                if response == answer:
                    print("The answer was correct!")
                    score += 1
                    break

                print(f"{n1} {self.operations[operation]} {n2} does not equal {response}.")
                print(f"The answer is {answer}.")
                break

        return score


    def test_5(self):

        score = 0

        for i in range(10):
            operation = randint(0, 5)

            n1 = 1
            n2 = 1

            if operation == 0:
                n1 = randint(1, 1000)
                n2 = randint(1, 1000)

            if operation == 1:
                n1 = randint(1, 1000)
                n2 = randint(1, n1)

            if operation == 2:
                n1 = randint(1, 20)
                n2 = randint(1, 20)

            if operation == 3:
                while True:
                    n1 = randint(1, 144)
                    n2 = randint(1, 12)
                    if n1 % n2 == 0:
                        break

            if operation == 4:
                n1 = randint(1, 20)
                n2 = randint(2, 3)

            if operation == 5:
                while True:
                    n1 = randint(1, 20)
                    n2 = 1 / randint(2, 3)
                    if (n1 ** n2) % 1 == 0:
                        break

            while True:
                print()
                response = input(f"What is {n1} {self.operations[operation]} {n2}? ")
                answer = int(eval(f"{n1}{self.operations[operation]}{n2}"))
                try:
                    response = int(response)
                except ValueError:
                    print("That is not a number! Try again.")
                    continue
                if response == answer:
                    print("The answer was correct!")
                    score += 1
                    break

                print(f"{n1} {self.operations[operation]} {n2} does not equal {response}.")
                print(f"The answer is {answer}.")
                break

        return score
