from random import randint

class Die():
    """Class of a die with six sides."""
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(num_sides):
        return randint(1, 6)