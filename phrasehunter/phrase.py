class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase
        self.phrase_set = set(phrase.lower())
        self.phrase_set.discard(' ')
        self.correct_guesses = []

    def display(self):
        display = ''
        for letter in self.phrase:
            if letter.lower() in set(self.correct_guesses):
                display += letter
            elif letter == ' ':
                display += ' '
            else:
                display += '_'
        return display

    def check_letter(self, guess):
        if guess in self.phrase_set:
            self.correct_guesses.append(guess)
            return True
        else:
            return False

    def check_complete(self):
        return len(self.phrase_set) == len(set(self.correct_guesses))


if __name__ == '__main__':
    phrase = Phrase('Foo Bar')
    print(phrase.phrase)
    print(phrase.phrase_set)
    print(f'display before guess: {phrase.display()}')
    phrase.check_letter('o')
    phrase.check_letter('z')
    print(f'display after guess: {phrase.display()}')
