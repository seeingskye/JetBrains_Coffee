class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = None

    def __str__(self):
        return f'''The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cups} of disposable cups
{self.money} of money'''

    def process(self, action):
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            print(self)
        elif action == "exit":
            return False
        return True

    def buy(self):
        global money
        coffee_type = input("What do you want to buy? 1 - espresso"
                            ", 2 - latte, 3 - cappuccino:")
        if coffee_type == "1":
            self.make_coffee(250, 0, 16, 4)
        elif coffee_type == "2":
            self.make_coffee(350, 75, 20, 7)
        elif coffee_type == "3":
            self.make_coffee(200, 100, 12, 6)
        elif coffee_type == "back":
            return None

    def make_coffee(self, water_used, milk_used, coffee_beans_used, cost):
        if self.water < water_used:
            print("Sorry, not enough water!")
        elif self.milk < milk_used:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < coffee_beans_used:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.water -= water_used
            self.milk -= milk_used
            self.coffee_beans -= coffee_beans_used
            self.disposable_cups -= 1
            self.money += cost
            print("I have enough resources, making you a coffee!")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add: "))
        self.milk += int(input("Write how many ml of milk do you want to add: "))
        self.coffee_beans += int(input("Write how many grams of coffee beans do you want to add: "))
        self.disposable_cups += int(input("Write how many disposable cups of coffee do you want to add: "))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


machine = CoffeeMachine(400, 540, 120, 9, 550)
power = True
while power:
    power = machine.process(input("Write action (buy, fill, take, remaining, exit)\n"))
