class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{}: {}'.format(self.name, self.description)


class Weapons(Items):
    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power