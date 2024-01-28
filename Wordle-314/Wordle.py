# File: Wordle.py

"""
Group 3-14
Hailey Bronson, McKenna Alder, Brian Stone, Alden Transfiguracion

This module contains the logic for the Wordle game.
"""

import tkinter as tk
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# Confetti animation code
def confetti_animation(canvas):
    colors = ["red", "green", "blue", "orange", "purple", "yellow"]
    
    for _ in range(100):
        x = random.randint(0, canvas.winfo_width())
        y = random.randint(0, canvas.winfo_height())
        color = random.choice(colors)
        
        size = random.randint(8, 10)
        confetti_shape = canvas.create_oval(x, y, x+size, y+size, fill=color, outline=color)
        
        # Remove the confetti after a few seconds
        canvas.after(1400, lambda c=canvas, s=confetti_shape: c.delete(s))

def wordle():
    # Chooses a random word from the dictionary
    solution_word = random.choice(FIVE_LETTER_WORDS)

    def enter_action(s, solution_word, gw):
        # Ensure s is a string
        if not isinstance(s, str):
            s = str(s)

        # Converts the input string to uppercase for consistency
        guess = s.upper()

        print(f"Guess: {guess}")
        print(f"Solution: {solution_word}")

        # Checks if the guess is in the list of valid words
        if guess.lower() in FIVE_LETTER_WORDS:
            # Iterate through each letter in the guess and compare with the solution
            for col, letter in enumerate(guess):
                if letter.upper() == solution_word[col].upper() or letter.lower() == solution_word[col].lower():
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    gw.set_key_color(letter.upper(), CORRECT_COLOR)  # Set key color to correct color
                elif letter.upper() in solution_word.upper():
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                    gw.set_key_color(letter.upper(), PRESENT_COLOR)  # Set key color to present color
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    gw.set_key_color(letter.upper(), MISSING_COLOR)  # Set key color to missing color

            # Move on to the next row
            current_row = gw.get_current_row()
            gw.set_current_row(current_row + 1)

            # Check if the user has correctly guessed all five letters
            if guess == solution_word.upper():
                gw.show_message("Wordle")
                
                # Start the confetti animation
                confetti_animation(gw._canvas)

            # Check if the game is finished (all rows filled)
            if gw.get_current_row() == N_ROWS:
                gw.show_message("Game over. You've reached the maximum number of attempts.")
        else:
            gw.show_message("Not in word list")



    def display_solution_word():
        # Displays the solution word in the first row of the window
        for col in range(N_COLS):
            gw.set_square_letter(0, col, solution_word[col].upper())

    gw = WordleGWindow()

    # Chooses a random word from the dictionary
    solution_word = random.choice(FIVE_LETTER_WORDS).upper()

    # Add an enter listener to handle user input
    gw.add_enter_listener(lambda s, solution_word=solution_word, gw=gw: enter_action(s, solution_word, gw))

    # Add a button listener to display the solution word when pressed
    gw.add_button("Show Solution", display_solution_word)

# Startup code
if __name__ == "__main__":
    wordle()






