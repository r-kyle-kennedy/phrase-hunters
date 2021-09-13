import random

from phrasehunter.phrase import Phrase
from phrasehunter import phrases


class Game():

    def __init__(self, name=None):
        self.missed = 0
        self.phrases = phrases.PHRASES
        self.active_phrase = None
        self.guesses = []
        self.player_name = name
        self.continue_game = 'y'

    def welcome(self):
        print('Welcome to the Phrase Guessing Game!!!')
        print('You have to guess all the letters in a random phrase.')
        print('If you guess an incorrect letter five times, you lose.')
        print('Guess all the letters in the phrase and you win!')
        print('Hint: the phrases are all about animals')
        if not self.player_name:
            self.player_name = input('Please enter your name:  ')

    def get_random_phrase(self):
        ## TODO: make sure a phrase isn't chosen twice in a row
        return Phrase(random.choice(self.phrases))

    def get_guess(self):
        guess = input('Guess a letter between a-z:  ').lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guesses:
                print(f'Woops looks like \'{guess}\' has already been guessed...')
                self.get_guess()
            else:
                self.guesses.append(guess)
                return guess
        else:
            print(f'Looks like \'{guess}\' is not a letter between a-z')
            self.get_guess()

    def game_over(self):
        print()
        if self.missed == 5:
            print('GAME OVER!!!')
            print(f'{self.player_name}, you didn\'t guess the phrase in less than 5 guesses...')
            print(f'The phrase was \'{self.active_phrase.phrase}\'.')
            self.continue_game = input('\nWould you like to play again?(Y/N)  ').lower()
        else:
            print(f'Congratulations {self.player_name}!!!')
            if self.missed != 1:
                print(f'You guessed the phrase with {self.missed} missed tries!')
            else:
                print(f'You guessed the phrase with {self.missed} missed try!')
            print(f'The phrase was \'{self.active_phrase.phrase}\'.')
            self.continue_game = input('\nWould you like to play again?(Y/N)  ').lower()

    def start(self):
        while self.continue_game == 'y':
            self.__init__(self.player_name)
            self.welcome()
            self.active_phrase = self.get_random_phrase()
            while self.missed < 5 and not self.active_phrase.check_complete():
                print(f'PHRASE: {self.active_phrase.display()}\n')
                current_guess = self.get_guess()
                if self.active_phrase.check_letter(current_guess):
                    print(f'YEA! \'{current_guess}\' is correct!')
                    letters_left = len(self.active_phrase.phrase_set)-len(self.active_phrase.correct_guesses)
                    if letters_left > 1:
                        print(f'You have {letters_left} more letters to go!\n')
                    elif letters_left > 0:
                        print(f'You have {letters_left} more letter to go!\n')
                else:
                    print(f'Uh Oh! \'{current_guess}\' is not correct...')
                    self.missed += 1
                    if self.missed < 4:
                        print(f'You have {5-self.missed} guesses left.\n')
                    elif self.missed < 5:
                        print(f'You have {5-self.missed} guess left! Don\'t mess up...\n')
            self.game_over()
        print('\nThanks for playing!!!\n')

if __name__ == '__main__':
    game = Game()
