import os
import tkinter as tk
from tkinter import messagebox

class UserCredentials:
    def __init__(self, root):
        self.root = root
        self.filename = os.path.join(os.path.expanduser('~'), 'Desktop', 'credentials.txt')
        self.create_widgets()

    def create_widgets(self):
        app_label = tk.Label(self.root, text="Application:")
        app_label.pack()
        self.app_entry = tk.Entry(self.root)
        self.app_entry.pack()

        username_label = tk.Label(self.root, text="Username:")
        username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        password_label = tk.Label(self.root, text="Password:")
        password_label.pack()
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        save_button = tk.Button(button_frame, text="Save", command=self.save_credentials, width=10)
        save_button.pack(side=tk.LEFT, padx=10, pady=11)
        
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, width=10)
        exit_button.pack(side=tk.RIGHT, padx=2, pady=11)

    def save_credentials(self):
        with open(self.filename, 'a') as f:
            f.write(f'\n\nApplication: {self.app_entry.get()}\nUsername: {self.username_entry.get()}\nPassword: {self.password_entry.get()}')
        messagebox.showinfo("Success", "Credentials saved successfully!")


def main():
    root = tk.Tk()
    app = UserCredentials(root)
    root.title("User Credentials")
    root.geometry("300x180")
    root.resizable(False, False)
    root.mainloop()
    
if __name__ == "__main__":
    main()
