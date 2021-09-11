from phrase import Phrase
import phrases


class Game():

    def __init__(self):
        self.missed = 0
        self.phrases = phrases.PHRASES
        self.active_phrase = None
        self.guesses = []
        self.player_name = None
        self.continue = 'y'

    def welcome(self):
        print('Welcome to the Phrase Guessing Game!!!')
        print('You have to guess all the letters in a random phrase.')
        print('If you guess an incorrect letter five times, you lose.')
        print('Guess all the letters in the phrase and you win!')
        if not self.player_name:
            self.player_name = input('Please enter your name:  ')


    def start(self):
        self.welcome()
        while self.continue == 'y':
            
