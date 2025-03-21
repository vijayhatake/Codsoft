import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")
        self.root.configure(bg="#f0f0f0")

        # Length input
        tk.Label(root, text="Password Length:", font=("Arial", 14), bg="#f0f0f0").pack(pady=5)
        self.length_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.length_entry.pack(pady=5)

        # Complexity options
        self.include_digits = tk.BooleanVar()
        self.include_special = tk.BooleanVar()

        tk.Checkbutton(root, text="Include Digits", variable=self.include_digits, bg="#f0f0f0", font=("Arial", 12)).pack()
        tk.Checkbutton(root, text="Include Special Characters", variable=self.include_special, bg="#f0f0f0", font=("Arial", 12)).pack()

        # Generate button
        tk.Button(root, text="Generate Password", command=self.generate_password, font=("Arial", 14), bg="#51c4d3", fg="white").pack(pady=10)

        # Display password
        self.result_label = tk.Label(root, text="", font=("Arial", 16), bg="#f0f0f0", wraplength=380)
        self.result_label.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 4:
                messagebox.showwarning("Warning", "Password length should be at least 4 characters.")
                return

            characters = string.ascii_letters
            if self.include_digits.get():
                characters += string.digits
            if self.include_special.get():
                characters += string.punctuation

            password = ''.join(random.choice(characters) for _ in range(length))
            self.result_label.config(text=f"Generated Password:\n{password}")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
