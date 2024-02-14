import random
import tkinter as tk
from tkinter import PhotoImage

randomNummber = random.randint(1, 20)
score = float('inf')
attempts = 0

def check_guess():
    global attempts 
    try:
        attempts += 1
        guess = int(guess_entry.get())
        if guess <= 0 or guess > 20:
            result_label.config(text="Enter a number between 1 and 20 🤦‍♂️")
        elif guess < randomNummber:
            result_label.config(text="Higher! 👍")
        elif guess > randomNummber:
            result_label.config(text="Lower! 👎")
        else:
            reset_game()
            result_label.config(text="You got! 🥳")
            
    except ValueError:
        result_label.config(text="Please enter a number #️⃣")

def reset_game():
    global randomNummber, score, attempts
    attempts = 0
    randomNummber = random.randint(1, 20)
    guess_entry.delete(0, 'end')
    result_label.config(text="")
    preview_label.config(text=randomNummber)

def scorekeeper():
    global score, attempts
    if attempts < score:
        score = attempts
    high_score_label.config(text=f"High Score: {score}")
    attempts_label.config(text=f"Attempts: {attempts}")


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x300")
root.resizable(False, False)

img = PhotoImage(file='logo.png')

img_label = tk.Label(root, image=img)
img_label.pack(pady=(10, 0))

preview_label = tk.Label(root, text=randomNummber, font=(None, 8, "bold"), fg="grey")
preview_label.pack()

high_score_label = tk.Label(root, text=f"High Score: {score if score != float('inf') else '0'}", font=(None, 12, "bold"), fg="green")
high_score_label.pack()

attempts_label = tk.Label(root, text=f"Attempts: {attempts}", font=(None, 12, "bold"), fg="orange")
attempts_label.pack()

guess_label = tk.Label(root, text="Guess a Number Between 1 & 20" , font=(None, 16, "bold"))
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

button_frame = tk.Frame(root)
button_frame.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=(10, 0))

check_button = tk.Button(root, text="Check", command=check_guess)
check_button.pack(side="left", padx=(50, 0))

check_button = tk.Button(root, text="Reset", command=reset_game)
check_button.pack(side="right", padx=(0, 50))



root.mainloop()

