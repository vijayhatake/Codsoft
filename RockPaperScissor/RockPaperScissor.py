import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")

        self.choices = ["Rock", "Paper", "Scissors"]
        self.user_score = 0
        self.computer_score = 0

        # Title
        tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=5)

        # Buttons for choices
        self.buttons_frame = tk.Frame(root, bg="#f0f0f0")
        self.buttons_frame.pack()

        tk.Button(self.buttons_frame, text="Rock", font=("Arial", 14), bg="#51c4d3", fg="white", width=10, command=lambda: self.play("Rock")).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Paper", font=("Arial", 14), bg="#51c4d3", fg="white", width=10, command=lambda: self.play("Paper")).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.buttons_frame, text="Scissors", font=("Arial", 14), bg="#51c4d3", fg="white", width=10, command=lambda: self.play("Scissors")).grid(row=0, column=2, padx=5, pady=5)

        # Result display
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        # Score display
        self.score_label = tk.Label(root, text="Score: You - 0 | Computer - 0", font=("Arial", 14), bg="#f0f0f0")
        self.score_label.pack(pady=5)

        # Play Again button
        tk.Button(root, text="Play Again", font=("Arial", 14), bg="#ffb74d", fg="black", command=self.reset_game).pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)

        # Game logic
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            result = f"You win! {user_choice} beats {computer_choice}."
            self.user_score += 1
        else:
            result = f"You lose! {computer_choice} beats {user_choice}."
            self.computer_score += 1

        self.result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")
        self.update_score()

    def update_score(self):
        self.score_label.config(text=f"Score: You - {self.user_score} | Computer - {self.computer_score}")

    def reset_game(self):
        self.result_label.config(text="")
        self.user_score = 0
        self.computer_score = 0
        self.update_score()

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
