import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300")

        self.tasks = []
        self.load_tasks()

        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE, bg="#f0f0f0", fg="#333")
        self.listbox.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.update_listbox()

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Add", command=self.add_task, width=12, bg="#51c4d3", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update", command=self.update_task, width=12, bg="#51c4d3", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_task, width=12, bg="#51c4d3", fg="white").pack(side="left", padx=5)
        tk.Button(btn_frame, text="Complete", command=self.mark_completed, width=12, bg="#51c4d3", fg="white").pack(side="left", padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[✔]" if task['completed'] else "[ ]"
            self.listbox.insert(tk.END, f"{status} {task['title']}")

    def get_selected_index(self):
        try:
            return self.listbox.curselection()[0]
        except IndexError:
            return None

    def add_task(self):
        title = simpledialog.askstring("Add Task", "Enter task title:")
        if title:
            self.tasks.append({"title": title, "completed": False})
            self.save_tasks()
            self.update_listbox()

    def update_task(self):
        index = self.get_selected_index()
        if index is not None:
            new_title = simpledialog.askstring("Update Task", "Enter new task title:", initialvalue=self.tasks[index]['title'])
            if new_title:
                self.tasks[index]['title'] = new_title
                self.save_tasks()
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
            if confirm:
                del self.tasks[index]
                self.save_tasks()
                self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        index = self.get_selected_index()
        if index is not None:
            self.tasks[index]['completed'] = not self.tasks[index]['completed']
            self.save_tasks()
            self.update_listbox()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
