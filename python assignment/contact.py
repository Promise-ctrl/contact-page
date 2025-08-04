import tkinter as tk
from tkinter import messagebox
import csv
import os

class ContactFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Form Application")
        self.root.geometry("400x300") # Set a default window size
        self.root.resizable(False, False) # Make the window non-resizable

        # Define the CSV file name
        self.csv_file = 'contacts.csv'

        # Create the header if the file doesn't exist
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Phone', 'Email'])

        self.create_widgets()

    def create_widgets(self):
        # Frame for input fields
        input_frame = tk.Frame(self.root, padx=20, pady=20)
        input_frame.pack(pady=10)

        # Name Label and Entry
        name_label = tk.Label(input_frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Phone Label and Entry
        phone_label = tk.Label(input_frame, text="Phone:")
        phone_label.grid(row=1, column=0, sticky="w", pady=5)
        self.phone_entry = tk.Entry(input_frame, width=30)
        self.phone_entry.grid(row=1, column=1, pady=5)

        # Email Label and Entry
        email_label = tk.Label(input_frame, text="Email:")
        email_label.grid(row=2, column=0, sticky="w", pady=5)
        self.email_entry = tk.Entry(input_frame, width=30)
        self.email_entry.grid(row=2, column=1, pady=5)

        # Save Button
        save_button = tk.Button(self.root, text="Save Contact", command=self.save_contact)
        save_button.pack(pady=10)

        # Message Label for feedback
        self.message_label = tk.Label(self.root, text="", fg="green")
        self.message_label.pack(pady=5)

    def save_contact(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        # Basic validation
        if not name or not phone or not email:
            self.message_label.config(text="All fields are required!", fg="red")
            return

        # Prepare data to be saved
        contact_data = [name, phone, email]

        try:
            # Open the CSV file in append mode
            with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(contact_data)
            self.message_label.config(text="Contact saved successfully!", fg="green")
            self.clear_fields()
        except IOError as e:
            self.message_label.config(text=f"Error saving contact: {e}", fg="red")
        except Exception as e:
            self.message_label.config(text=f"An unexpected error occurred: {e}", fg="red")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        
 def open_github_link(self, event):
        # visit my Github page
        webbrowser.open_new("https://github.com/Promise-ctrl/contact-page/upload/main")

# Main part of the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactFormApp(root)
    root.mainloop()
