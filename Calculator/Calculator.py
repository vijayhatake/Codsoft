import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.configure(bg="#f0f0f0")

        self.result_var = tk.StringVar()

        # Entry widget to display input and result
        self.entry = tk.Entry(root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
        self.entry.pack(fill="both", padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        self.create_buttons(buttons)

    def create_buttons(self, buttons):
        grid_frame = tk.Frame(self.root)
        grid_frame.pack()

        row, col = 0, 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(grid_frame, text=button, font=("Arial", 18), bg="#51c4d3", fg="white", width=5, height=2, command=action).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.result_var.set("")
        elif button == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
