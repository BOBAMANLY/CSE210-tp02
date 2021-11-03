import random

# TODO: Define the Thrower class here.

class Dealer:
    def __init__(self):
        self.dice = []
        self.num_throws = 0

    def can_throw(self):
        if (self.dice.count(5) > 0 or self.dice.count(1) > 0 or self.num_throws == 0):
            return True
        else:
            return False

    def get_points(self):
        fives = self.dice.count(5) * 50
        ones = self.dice.count(1) * 100
        return fives + ones

    def throw_dice(self):
        self.dice.clear()
        for _ in range(0, 5):
            num = random.randint(1,6)
            self.dice.append(num)
        self.num_throws += 1