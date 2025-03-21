import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import json

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.contacts = []
        self.load_contacts()

        # Title
        tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=5)

        # Contact List
        self.contact_treeview = ttk.Treeview(root, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.contact_treeview.heading("Name", text="Name")
        self.contact_treeview.heading("Phone", text="Phone")
        self.contact_treeview.heading("Email", text="Email")
        self.contact_treeview.heading("Address", text="Address")
        self.contact_treeview.pack(pady=10)

        self.update_contact_treeview()

        # Buttons
        tk.Button(root, text="Add Contact", bg="#51c4d3", fg="white", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="Update Contact", bg="#51c4d3", fg="white", command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", bg="#51c4d3", fg="white", command=self.delete_contact).pack(pady=5)
        tk.Button(root, text="Search Contact", bg="#51c4d3", fg="white", command=self.search_contact).pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def load_contacts(self):
        try:
            with open('contacts.json', 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open('contacts.json', 'w') as file:
            json.dump(self.contacts, file, indent=2)

    def update_contact_treeview(self):
        self.contact_treeview.delete(*self.contact_treeview.get_children())
        for contact in self.contacts:
            self.contact_treeview.insert("", tk.END, values=(contact['name'], contact['phone'], contact.get('email', ''), contact.get('address', '')))

    def get_selected_index(self):
        selected_item = self.contact_treeview.selection()
        if selected_item:
            index = self.contact_treeview.index(selected_item[0])
            return index if 0 <= index < len(self.contacts) else None
        return None

    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        if name:
            phone = simpledialog.askstring("Add Contact", "Enter phone number:")
            email = simpledialog.askstring("Add Contact", "Enter email (optional):")
            address = simpledialog.askstring("Add Contact", "Enter address (optional):")

            new_contact = {"name": name, "phone": phone}
            if email:
                new_contact["email"] = email
            if address:
                new_contact["address"] = address

            self.contacts.append(new_contact)
            self.save_contacts()
            self.update_contact_treeview()

    def update_contact(self):
        index = self.get_selected_index()
        if index is not None:
            contact = self.contacts[index]
            name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact['name'])
            phone = simpledialog.askstring("Update Contact", "Enter new phone:", initialvalue=contact['phone'])
            email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.get('email', ''))
            address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.get('address', ''))

            if name and phone:
                self.contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
                self.save_contacts()
                self.update_contact_treeview()
        else:
            messagebox.showwarning("Invalid Selection", "Please select a contact to update.")

    def delete_contact(self):
        index = self.get_selected_index()
        if index is not None:
            confirm = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
            if confirm:
                del self.contacts[index]
                self.save_contacts()
                self.update_contact_treeview()
        else:
            messagebox.showwarning("Invalid Selection", "Please select a contact to delete.")

    def search_contact(self):
        query = simpledialog.askstring("Search Contact", "Enter name or phone:")
        if query:
            results = [c for c in self.contacts if query.lower() in c['name'].lower() or query in c['phone']]
            if results:
                result_text = "\n".join([f"{c['name']} - {c['phone']}" for c in results])
                messagebox.showinfo("Search Results", result_text)
            else:
                messagebox.showinfo("Search Results", "No matching contact found.")

    def on_close(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
