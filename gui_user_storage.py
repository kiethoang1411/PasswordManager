import os
import tkinter as tk
from tkinter import messagebox

class UserCredentials:
    def __init__(self, filename):
        self.filename = os.path.join(os.path.expanduser('~'), 'Desktop', filename)

    def add_credentials(self, app_name, username, password):
        with open(self.filename, 'a') as f:
            f.write(f'\n\nApplication: {app_name}\nUsername: {username}\nPassword: {password}')

def user_interface():
    uc = UserCredentials('credentials.txt')

    root = tk.Tk()
    root.title("User Credentials")  
    root.geometry("200x200")  

    app_label = tk.Label(root, text="Application:")
    app_label.pack()
    app_entry = tk.Entry(root)
    app_entry.pack()

    username_label = tk.Label(root, text="Username:")
    username_label.pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    password_label = tk.Label(root, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(root, show='*')
    password_entry.pack()

    def save_credentials():
        uc.add_credentials(app_entry.get(), username_entry.get(), password_entry.get())
        messagebox.showinfo("Success", "Credentials saved successfully!")

    button_frame = tk.Frame(root)
    button_frame.pack()

    save_button = tk.Button(button_frame, text="Save", command=save_credentials)
    save_button.pack(side=tk.LEFT)

    exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
    exit_button.pack(side=tk.LEFT)

    root.mainloop()

# Run the user interface
user_interface()
