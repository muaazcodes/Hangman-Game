import Hangman_stages
import Words
import random

class HangmanGame:
    def __init__(self):
        self.lines = 6
        self.chosen_word = random.choice(Words.word_list).lower()
        self.display = ["_"] * len(self.chosen_word)
        self.game_over = False
        self.message = ""
        self.guessed_letters = set()

    def get_display_word(self):
        return " ".join(self.display)

    def get_stage(self):
        return Hangman_stages.HANGMAN_STAGES[self.lines]

    def guess_letter(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            self.message = f"You already guessed '{letter}'."
            return
        self.guessed_letters.add(letter)

        if letter in self.chosen_word:
            for i, l in enumerate(self.chosen_word):
                if l == letter:
                    self.display[i] = letter
            if "_" not in self.display:
                self.game_over = True
                self.message = "You win!!"
            
        else:
            self.lines -= 1
            if self.lines == 0:
                self.game_over = True
                self.message = f"You lose!!."
            else:
                self.message = f"Wrong guess. Lives left: {self.lines}"

    def guess_word(self, word):
        word = word.lower()
        if word == self.chosen_word:
            self.display = list(self.chosen_word)
            self.game_over = True
            self.message = "You win!!"
        else:
            self.lines -= 1
            if self.lines == 0:
                self.game_over = True
                self.message = f"You lose!! The word was '{self.chosen_word}'."
            else:
                self.message = f"Wrong word guess. Lives left: {self.lines}"

    def is_over(self):
        return self.game_over

    def get_message(self):
        return self.message

