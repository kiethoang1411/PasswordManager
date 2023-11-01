import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

rule_upper = {
    'A': 'ZY', 'B': 'YX', 'C': 'XV', 'D': 'VT', 'E': 'TS',
    'F': 'SR', 'G': 'RQ', 'H': 'QP', 'I': 'PO', 'J': 'ON',
    'K': 'NM', 'L': 'ML', 'M': 'LK', 'N': 'KJ', 'O': 'JI',
    'P': 'IH', 'Q': 'HG', 'R': 'GF', 'S': 'FE', 'T': 'ED',
    'U': 'DC', 'V': 'CB', 'W': 'BA', 'X': 'AZ', 'Y': 'ZA',
    'Z': 'AB'
}

rule_lower = {
    'a': 'zy', 'b': 'yx', 'c': 'xv', 'd': 'vt', 'e': 'ts',
    'f': 'sr', 'g': 'rq', 'h': 'qp', 'i': 'po', 'j': 'on',
    'k': 'nm', 'l': 'ml', 'm': 'lk', 'n': 'kj', 'o': 'ji',
    'p': 'ih', 'q': 'hg', 'r': 'gf', 's': 'fe', 't': 'ed',
    'u': 'dc', 'v': 'cb', 'w': 'ba', 'x': 'az'
}

# Custom rule for numbers
custom_number_rule = {
    '1': 'μ', '2': 'π', '3': 'φ', '4': 'ψ', '5': '𐌈',
    '6': '𐌙', '7': '𐌒', '8': '𐌎', '9': '𐌞', '0': 'ω'
}


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

        decode_button = tk.Button(button_frame, text="Decode", command=self.decode_credentials, width=10)
        decode_button.pack(side=tk.LEFT, padx=10, pady=11)

        exit_button = tk.Button(button_frame, text="Exit", command=self.root.quit, width=10)
        exit_button.pack(side=tk.RIGHT, padx=2, pady=11)

    def encode_text(self, text):
        encoded_text = ""
        for char in text:
            if char.isupper() and char in rule_upper:
                encoded_text += rule_upper[char]
            elif char.islower() and char in rule_lower:
                encoded_text += rule_lower[char]
            elif char.isdigit() and char in custom_number_rule:
                encoded_text += custom_number_rule[char]  # Use custom rule for numbers
            else:
                encoded_text += char
        return encoded_text

    def decode_text(self, text):
        decoded_text = ""
        i = 0
        while i < len(text):
            char = text[i]
            if char.isupper() and i + 1 < len(text) and text[i:i+2] in rule_upper.values():
                decoded_text += [c for c, code in rule_upper.items() if code == text[i:i+2]][0]
                i += 2
            elif char.islower() and i + 1 < len(text) and text[i:i+2] in rule_lower.values():
                decoded_text += [c for c, code in rule_lower.items() if code == text[i:i+2]][0]
                i += 2
            elif char in custom_number_rule.values():
                # Reverse custom rule for numbers
                decoded_text += [digit for digit, symbol in custom_number_rule.items() if symbol == char][0]
                i += 1
            else:
                decoded_text += char
                i += 1
        return decoded_text

    def decode_credentials(self):
        # Open file dialog to select the file
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

        if not filepath:  # If no file is selected
            return

        # Read the file content
        with open(filepath, 'r') as f:
            encoded_text = f.read()

        # Decode the text using your custom rule
        decoded_text = self.decode_text(encoded_text)

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
        encoded_credentials = f'\n\nApplication: {self.encode_text(self.app_entry.get())}\nUsername: {self.encode_text(self.username_entry.get())}\nPassword: {self.encode_text(self.password_entry.get())}'
        with open(self.filename, 'a') as f:
            f.write(encoded_credentials)
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
