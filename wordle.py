import tkinter as tk
import random
from collections import Counter

# ---------------------------------------------------
# SETTINGS
# ---------------------------------------------------

ROWS = 6
COLS = 5

BACKGROUND = "#121213"
EMPTY = "#3A3A3C"
GREEN = "#538D4E"
YELLOW = "#B59F3B"
GREY = "#3A3A3C"
TEXT = "#FFFFFF"

guess_number = 0
keyboard_buttons = {}

# ---------------------------------------------------
# LOAD WORDS
# ---------------------------------------------------

with open("c:/Users/Dell/Downloads/Five_letterwords_new.txt") as file:
    words = file.read()

word_list = [
    word.strip().lower()
    for word in words.split("\n")
    if len(word.strip()) == 5
]

chosen_word = random.choice(word_list)

# Uncomment this line while testing.
# print(chosen_word)

# ---------------------------------------------------
# WINDOW
# ---------------------------------------------------

window = tk.Tk()
window.title("Wordle")
window.geometry("500x800")
window.configure(bg=BACKGROUND)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

title = tk.Label(
    window,
    text="WORDLE",
    bg=BACKGROUND,
    fg=TEXT,
    font=("Arial", 28, "bold")
)

title.pack(pady=20)

# ---------------------------------------------------
# MESSAGE LABEL
# ---------------------------------------------------

message = tk.Label(
    window,
    text="",
    bg=BACKGROUND,
    fg="white",
    font=("Arial", 12)
)

message.pack()

# ---------------------------------------------------
# GRID
# ---------------------------------------------------

grid_frame = tk.Frame(window, bg=BACKGROUND)
grid_frame.pack(pady=20)

tiles = []

for row in range(ROWS):

    tile_row = []

    for column in range(COLS):

        tile = tk.Label(
            grid_frame,
            text="",
            width=3,
            height=1,
            font=("Arial", 24, "bold"),
            bg=BACKGROUND,
            fg="white",
            relief="solid",
            borderwidth=2
        )

        tile.grid(row=row, column=column, padx=4, pady=4)

        tile_row.append(tile)

    tiles.append(tile_row)

# ---------------------------------------------------
# INPUT BOX
# ---------------------------------------------------

entry = tk.Entry(
    window,
    width=10,
    justify="center",
    font=("Arial", 20, "bold")
)

entry.pack(pady=10)

# ---------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------


def add_letter(letter):
    current = entry.get()

    if len(current) < 5:
        entry.insert(tk.END, letter)


def delete_letter():
    current = entry.get()

    if len(current) > 0:
        entry.delete(len(current) - 1, tk.END)


def update_key(letter, colour):

    button = keyboard_buttons[letter]

    if button["bg"] == GREEN:
        return

    if button["bg"] == YELLOW and colour == GREY:
        return

    button.config(bg=colour)


def guess_word():
    global guess_number

    guessed_word = entry.get().lower()

    if len(guessed_word) != 5:
        message.config(text="Enter a five-letter word.")
        return

    if guessed_word not in word_list:
        message.config(text="Word not found.")
        return

    colours = [GREY] * 5
    remaining = Counter(chosen_word)

    # Green letters

    for i in range(5):
        if guessed_word[i] == chosen_word[i]:
            colours[i] = GREEN
            remaining[guessed_word[i]] -= 1

    # Yellow letters

    for i in range(5):
        if colours[i] == GREY:
            if remaining[guessed_word[i]] > 0:
                colours[i] = YELLOW
                remaining[guessed_word[i]] -= 1

    # Display tiles

    for i in range(5):

        tiles[guess_number][i].config(
            text=guessed_word[i].upper(),
            bg=colours[i]
        )

        update_key(guessed_word[i].upper(), colours[i])

    # Win condition

    if guessed_word == chosen_word:
        message.config(text="Congratulations!")

        guess_button.config(state="disabled")
        entry.config(state="disabled")

        return

    guess_number += 1

    if guess_number >= ROWS:
        message.config(
            text=f"The word was {chosen_word.upper()}"
        )

        guess_button.config(state="disabled")
        entry.config(state="disabled")

    entry.delete(0, tk.END)


# ---------------------------------------------------
# KEYBOARD
# ---------------------------------------------------

keyboard_frame = tk.Frame(window, bg=BACKGROUND)
keyboard_frame.pack(pady=20)

keyboard_rows = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

for letters in keyboard_rows:

    row_frame = tk.Frame(
        keyboard_frame,
        bg=BACKGROUND
    )

    row_frame.pack(pady=3)

    for letter in letters:

        button = tk.Button(
            row_frame,
            text=letter,
            width=4,
            height=2,
            font=("Arial", 10, "bold"),
            bg=EMPTY,
            fg="white",
            relief="flat",
            command=lambda l=letter: add_letter(
                l.lower()
            )
        )

        button.pack(side="left", padx=2)

        keyboard_buttons[letter] = button

# ---------------------------------------------------
# ENTER AND BACKSPACE
# ---------------------------------------------------

bottom_frame = tk.Frame(
    keyboard_frame,
    bg=BACKGROUND
)

bottom_frame.pack(pady=10)

enter_button = tk.Button(
    bottom_frame,
    text="ENTER",
    width=8,
    height=2,
    font=("Arial", 10, "bold"),
    command=guess_word
)

enter_button.pack(side="left", padx=5)

backspace_button = tk.Button(
    bottom_frame,
    text="⌫",
    width=5,
    height=2,
    font=("Arial", 12, "bold"),
    command=delete_letter
)

backspace_button.pack(side="left", padx=5)

# ---------------------------------------------------
# ALLOW THE ENTER KEY TO SUBMIT A GUESS
# ---------------------------------------------------

window.bind("<Return>", lambda event: guess_word())

# ---------------------------------------------------
# START PROGRAM
# ---------------------------------------------------

window.mainloop()