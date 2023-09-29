# Import tkinter module
import tkinter as tk
import string
import random
import pyperclip
from tkinter import messagebox

# Define the class for the password generator
class PasswordGenerator:
    # Define the constructor method
    def __init__(self, master):
        # Set the master window
        self.master = master
        self.master.title("Generator")
        self.master.resizable(False, False)

        # Create a label for the length selection
        self.length_label = tk.Label(self.master, text="Select the length of the password (minimum length is 8):")
        self.length_label.grid(row=0, column=0, columnspan=2, sticky="W")
        
        # Create a scale widget for the length selection
        self.length_scale = tk.Scale(self.master, from_=8, to=64, orient=tk.HORIZONTAL)
        self.length_scale.grid(row=1, column=0, columnspan=2)

        # Create boolean variables for the character types
        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()
        self.var4 = tk.BooleanVar()
        self.var5 = tk.BooleanVar()

        # Create checkbuttons for the character types
        self.check1 = tk.Checkbutton(self.master, text="Include lowercase letters", variable=self.var1)
        self.check1.grid(row=2, column=0, sticky="W")

        self.check2 = tk.Checkbutton(self.master, text="Include uppercase letters", variable=self.var2)
        self.check2.grid(row=3, column=0, sticky="W")

        self.check3 = tk.Checkbutton(self.master, text="Include numbers", variable=self.var3)
        self.check3.grid(row=4, column=0, sticky="W")

        self.check4 = tk.Checkbutton(self.master, text="Include special characters (no spaces)", variable=self.var4)
        self.check4.grid(row=5, column=0, sticky="W")

        self.check5 = tk.Checkbutton(self.master, text="Include special characters and spaces", variable=self.var5)
        self.check5.grid(row=6, column=0, sticky="W")

        # Create a button to generate the password
        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=7, column=0)
        
        # Create a button to copy the password to the clipboard
        self.copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=1)

        # Create an entry widget to display the password
        self.password_entry = tk.Entry(self.master, fg="blue")
        self.password_entry.config(state="readonly")
        self.password_entry.grid(row=8, column=0)

    # Define the method to generate the password
    def generate_password(self):
        # Get the password length from the scale widget
        password_length = self.length_scale.get()

        # Create an empty list for the character types
        character_types = []

        # Append the character types based on the checkbuttons
        if self.var1.get():
            character_types.append(string.ascii_lowercase)
        
        if self.var2.get():
            character_types.append(string.ascii_uppercase)
        
        if self.var3.get():
            character_types.append(string.digits)
        
        if self.var4.get():
            character_types.append(string.punctuation)
        
        if self.var5.get():
            character_types.append(string.punctuation + string.whitespace)

        # Check if at least one character type is selected
        if not character_types:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        # Check if the password length is valid
        if password_length < 8:
            messagebox.showerror("Error", "Password length must be at least 8 characters.")
            return

        # Create an empty list to store character types to ensure one character from each type is included
        selected_character_types = []

        # Create a password with at least one character from each selected character type
        password = ""

        # Ensure at least one character from each selected character type
        for char_type in character_types:
            selected_character = random.choice(char_type)
            selected_character_types.append(char_type)
            password += selected_character

        # Fill the remaining password length with random characters from the selected character types
        remaining_length = password_length - len(password)
        if remaining_length > 0:
            for _ in range(remaining_length):
                char_type = random.choice(selected_character_types)
                password += random.choice(char_type)

        # Shuffle the generated password to randomize the character order
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        # Set the width of the entry widget to a minimum of 20 characters or the password length, whichever is larger
        self.password_entry.config(width=max(20, len(password)))

        # Enable the entry widget to insert the password
        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

        # Disable the entry widget to prevent editing
        self.password_entry.config(state="readonly")
        
    # Define a method to copy the password to the clipboard
    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Info", "Password copied to clipboard!")
        else:
            messagebox.showerror("Error", "No password to copy!")


def main():
    root = tk.Tk()
    generator = PasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()