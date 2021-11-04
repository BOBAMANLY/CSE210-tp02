import random

# TODO: Define the Dealer class here.

class Dealer:
    def __init__(self):
        self.current_card = 0
        self.next_card = 0
        self.user_input = ""
        self.points = 300

    def can_deal(self):
        if self.points > 0 and self.user_input != "q":
            return True

    def total_points(self):
        if self.user_input == "h" and self.next_card > self.current_card:
            self.points += 100
        elif self.user_input == "l" and self.next_card < self.current_card:
            self.points += 100
        else:
            self.points -= 75
        return self.points

    def draw_current_card(self):
        self.current_card = random.randint(1,13)
        return self.current_card

    def draw_next_card(self):
        self.next_card = random.randint(1,13)
        while self.next_card == self.current_card:
            self.next_card = random.randint(1,13)
        return self.next_card

    def get_guess(self):
        self.user_input = input("Is the next card higher or lower(h/l)? ")
        return self.user_input