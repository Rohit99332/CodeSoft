import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=10)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=10)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=10)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=10)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.contacts_listbox = tk.Listbox(root)
        self.contacts_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.contacts_listbox.bind('<<ListboxSelect>>', self.display_contact_details)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=6, column=0, pady=10)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=6, column=1, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
            self.update_contacts_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and Phone are required!")

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, contact['name'])

    def display_contact_details(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact['address'])

    def update_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            contact['name'] = self.name_entry.get()
            contact['phone'] = self.phone_entry.get()
            contact['email'] = self.email_entry.get()
            contact['address'] = self.address_entry.get()
            self.update_contacts_listbox()
            self.clear_entries()

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.update_contacts_listbox()
            self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
