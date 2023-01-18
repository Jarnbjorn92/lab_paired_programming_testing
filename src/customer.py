class Customer:
    def __init__(self, name, wallet, age, drunkeness):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = drunkeness

    def buy_drink(self, amount):
        self.wallet -= amount

    def age_check(self):
        self.age >= 18

    def increase_drunkeness(self, alcohol_level):
        self.drunkenness += alcohol_level

        