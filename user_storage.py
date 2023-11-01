import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import string
    
def rot5(text):
    rot5_trans = str.maketrans(string.digits, '5678901234')
    return text.translate(rot5_trans)

def rot13(text):
    rot13_trans = str.maketrans(
        "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
        "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
    )
    return text.translate(rot13_trans)

def reverse_rot5(text):
    return rot5(text)  # ROT5 is its own inverse


def reverse_rot13(text):
    return rot13(text)  # ROT13 is its own inverse


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
        
        decode_button = tk.Button(self.root, text="Decode File", command=self.decode_credentials, width=10)
        decode_button.pack(pady=5)
        
        exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, width=10)
        exit_button.pack(side=tk.RIGHT, padx=2, pady=11)
    
    def decode_credentials(self):
        # Open file dialog to select the file
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if not filepath:  # If no file is selected
            return

        # Read the file content
        with open(filepath, 'r') as f:
            encoded_text = f.read()

        # Decode the text
        decoded_text = reverse_rot5(reverse_rot13(encoded_text))

        # Delete the encoded file
        os.remove(filepath)

        # Set the save path to "credentials.txt" on the desktop
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        save_path = os.path.join(desktop_path, "credentials.txt")

        # Save the decoded text to the new file
        with open(save_path, 'w') as f:
            f.write(decoded_text)

        messagebox.showinfo("Success", f"File decoded and saved as {save_path}!")


    def save_credentials(self):
            with open(self.filename, 'a') as f:
                f.write(rot13(rot5(f'\n\nApplication: {self.app_entry.get()}\nUsername: {self.username_entry.get()}\nPassword: {self.password_entry.get()}')))
            messagebox.showinfo("Success", "Credentials saved successfully on Desktop!")
            

def main():
    root = tk.Tk()
    app = UserCredentials(root)
    root.title("User Credentials")
    root.geometry("300x200")
    root.resizable(False, False)
    root.mainloop()
    
if __name__ == "__main__":
    main()
