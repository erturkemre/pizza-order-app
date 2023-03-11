import pizza_classes
class Decorator(pizza_classes.Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + pizza_classes.Pizza.get_cost(self)

    def get_description(self):
        return pizza_classes.Pizza.get_description(self)


class Zeytin(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 3.0

class Mantarlar(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantarlar"
        self.cost = 7.0

class KeciPeyniri(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 7.0

class Et(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 10.0

class Sogan(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
        self.cost = 3.5

class Misir(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 2.5