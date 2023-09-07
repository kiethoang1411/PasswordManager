import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    password_length = length_scale.get()
    character_types = []
    if var1.get():
        character_types.append(string.ascii_lowercase)
    if var2.get():
        character_types.append(string.ascii_uppercase)
    if var3.get():
        character_types.append(string.digits)
    if var4.get():
        character_types.append(string.punctuation)
    if var5.get():
        character_types.append(string.punctuation + string.whitespace)
    
    if password_length >= 8 and character_types:
        characters = "".join(character_types)
        password = "".join(random.choice(characters) for _ in range(password_length))
        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")
    else:
        messagebox.showerror("Error", "Invalid input. Please select a length greater than or equal to 8 and select at least one character type.")

root = tk.Tk()
root.title("Generator")
root.resizable(False, False)

length_label = tk.Label(root, text="Select the length of the password (minimum length is 8):")
length_label.grid(row=0, column=0, columnspan=2, sticky="W")
length_scale = tk.Scale(root, from_=8, to=64, orient=tk.HORIZONTAL)
length_scale.grid(row=1, column=0, columnspan=2)

var1 = tk.BooleanVar()
check1 = tk.Checkbutton(root, text="Include lowercase letters", variable=var1)
check1.grid(row=2, column=0, sticky="W")

var2 = tk.BooleanVar()
check2 = tk.Checkbutton(root, text="Include uppercase letters", variable=var2)
check2.grid(row=3, column=0, sticky="W")

var3 = tk.BooleanVar()
check3 = tk.Checkbutton(root, text="Include numbers", variable=var3)
check3.grid(row=4, column=0, sticky="W")

var4 = tk.BooleanVar()
check4 = tk.Checkbutton(root, text="Include special characters (no spaces)", variable=var4)
check4.grid(row=5, column=0, sticky="W")

var5 = tk.BooleanVar()
check5 = tk.Checkbutton(root, text="Include special characters and spaces", variable=var5)
check5.grid(row=6, column=0, sticky="W")

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=7, column=0)

password_entry = tk.Entry(root, fg="blue")
password_entry.config(state="readonly")
password_entry.grid(row=8, column=0)

root.mainloop()
