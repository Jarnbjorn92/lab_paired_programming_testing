class Pub:
    def __init__(self, name, till, drinks):
        self.name = name
        self.till = till
        self.drinks = drinks

    def increase_till(self, amount):
        self.till += amount

    def refuse_service(self, drunnkeness):
        if drunnkeness > 10:
            return 'No service'
        else:
            return 'Your ok'
