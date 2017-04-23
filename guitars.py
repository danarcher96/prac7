

class Guitars:

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost


    def __str__(self):
        return "{} ({}) : ${.2f}".format(self.name, self.year, self.cost)

    def get_age(self, year):
        guitar_age = year - self.year
        return guitar_age

    def is_vintage(self, year):

        guitar_age = year - self.year

        if guitar_age >= 50:
            return True
        else:
            return False


