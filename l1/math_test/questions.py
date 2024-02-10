from random import randint


class MathTestConstructor:
    def __init__(self):
        self.difficulty = 3

        self.operations = ["+", "-", "*", "/", "**", "**"]
        self.correct_msg = "The answer is correct!"
        self.valueerror_msg = "That is not an integer! Try again."

        self.n1 = 0
        self.n2 = 0
        self.operation = "+"

        self.score = 0

    def test_builder(self):
        self.n1 = 0
        self.n2 = 0

        while True:
            if self.difficulty == 1:
                self.operation = randint(0, 1)
                if self.operation == 0:
                    self.n1 = randint(1, 10)
                    self.n2 = randint(1, 10)
                elif self.operation == 1:
                    self.n1 = randint(1, 10)
                    self.n2 = randint(1, self.n1)

            elif self.difficulty == 2:
                self.operation = randint(0, 3)
                if self.operation == 0:
                    self.n1 = randint(1, 50)
                    self.n2 = randint(1, 50)
                elif self.operation == 1:
                    self.n1 = randint(1, 50)
                    self.n2 = randint(1, self.n1)
                elif self.operation == 2:
                    self.n1 = randint(1, 5)
                    self.n2 = randint(1, 12)
                elif self.operation == 3:
                    while True:
                        self.n1 = randint(1, 60)
                        self.n2 = randint(1, 12)
                        if self.n1 % self.n2 == 0:
                            break

            elif self.difficulty == 3:
                self.operation = randint(0, 3)
                if self.operation == 0:
                    self.n1 = randint(1, 100)
                    self.n2 = randint(1, 100)
                elif self.operation == 1:
                    self.n1 = randint(1, 100)
                    self.n2 = randint(1, self.n1)
                elif self.operation == 2:
                    self.n1 = randint(1, 12)
                    self.n2 = randint(1, 12)
                elif self.operation == 3:
                    while True:
                        self.n1 = randint(1, 144)
                        self.n2 = randint(1, 12)
                        if self.n1 % self.n2 == 0:
                            break

            elif self.difficulty == 4:
                self.operation = randint(0, 5)
                if self.operation == 0:
                    self.n1 = randint(1, 500)
                    self.n2 = randint(1, 500)
                elif self.operation == 1:
                    self.n1 = randint(1, 500)
                    self.n2 = randint(1, self.n1)
                elif self.operation == 2:
                    self.n1 = randint(1, 15)
                    self.n2 = randint(1, 15)
                elif self.operation == 3:
                    while True:
                        self.n1 = randint(1, 225)
                        self.n2 = randint(1, 15)
                        if self.n1 % self.n2 == 0:
                            break
                elif self.operation == 4:
                    self.n1 = randint(1, 12)
                    self.n2 = 2
                elif self.operation == 5:
                    while True:
                        self.n1 = randint(1, 12)
                        self.n2 = 1 / 2
                        if (self.n1 ** self.n2) % 1 == 0:
                            break

            elif self.difficulty == 5:
                self.operation = randint(0, 5)
                if self.operation == 0:
                    self.n1 = randint(1, 1000)
                    self.n2 = randint(1, 1000)
                elif self.operation == 1:
                    self.n1 = randint(1, 1000)
                    self.n2 = randint(1, self.n1)
                elif self.operation == 2:
                    self.n1 = randint(1, 20)
                    self.n2 = randint(1, 20)
                elif self.operation == 3:
                    while True:
                        self.n1 = randint(1, 400)
                        self.n2 = randint(1, 20)
                        if self.n1 % self.n2 == 0:
                            break
                elif self.operation == 4:
                    self.n1 = randint(1, 20)
                    self.n2 = randint(2, 3)
                elif self.operation == 5:
                    while True:
                        self.n1 = randint(1, 20)
                        self.n2 = 1 / randint(2, 3)
                        if (self.n1 ** self.n2) % 1 == 0:
                            break

            if self.n1 and self.n2:
                break

    def test(self):
        self.score = 0

        for i in range(10):
            self.test_builder()
            while True:
                response = input(f"""
\nWhat is {self.n1} {self.operations[int(self.operation)]} {self.n2}? """)
                answer = int(eval(f"""
{self.n1}{self.operations[int(self.operation)]}{self.n2}"""))
                try:
                    response = int(response)
                except ValueError:
                    print(self.valueerror_msg)
                    continue
                if response == answer:
                    print(self.correct_msg)
                    self.score += 1
                else:
                    print(f"""
{self.n1} {self.operations[int(self.operation)]} {self.n2} does not equal {response}.""")
                    print(f"The answer is {answer}.")
                break
