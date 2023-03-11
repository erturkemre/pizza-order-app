# encoding:utf-8

class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class Klasik(Pizza):
    def __init__(self):
        super().__init__("Klasik pizza", 50.0)


class Margherita(Pizza):
    def __init__(self):
        super().__init__("Margherita pizza", 55.0)

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Türk pizzası", 60.0)

class Dominos(Pizza):
    def __init__(self):
        super().__init__("Dominos pizza", 65.0)

