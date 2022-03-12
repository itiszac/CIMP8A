class Db:
    def __init__(self, filename):
        self.filename = filename
        self.money = 0.0

        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as file:
                self.money = float(file.readline())
                if self.money < 5:
                    print("You don't have enough to play, resetting back to $1,000.")
                    self.save(money=1000)
                print("Money", self.money)
                print()
        except FileNotFoundError as e:
            print("You don't have a save file. Creating a new one and starting with $1,000.")
            self.save(money=1000)
        except Exception as e:
            print(type(e), e)

    def save(self, money):
        try:
            with open(self.filename, "w") as file:
                file.write(str(money))
                self.money = money
        except Exception as e:
            print(type(e), e)
