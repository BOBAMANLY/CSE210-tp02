from game.dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """ 
        self.keep_playing = True
        self.score = 0
        self.dealer = Dealer()

        self.current_card = 0
        self.next_card = 0
        self.guess = ""

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the dice.

        Args:
            self (Director): An instance of Director.
        """
        current_card = self.dealer.draw_current_card()
        print(f'Current card is {current_card}')
        guess_card = self.dealer.get_guess()
        next_card = self.dealer.draw_next_card()

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        points = 0
        points = self.dealer.total_points()
        self.score = points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card was: {self.dealer.next_card}")
        print(f"Your score is: {self.score}")
        if self.dealer.can_deal():
            choice = input("Play again? [y/n] ")
            self.keep_playing = (choice == "y")
            print()
        else:
            self.keep_playing = False