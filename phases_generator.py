import tkinter as tk
import secrets
import pyperclip
from tkinter import messagebox  # Import the messagebox module

class PassphraseGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Passphrase Generator")

        # Create a main frame
        self.main_frame = tk.Frame(self.master)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Centered "Number of words" label
        self.word_count_label = tk.Label(self.main_frame, text="Number of words:")
        self.word_count_label.grid(row=0, column=0, padx=(20, 5), pady=10, sticky=tk.W)

        # Centered Spinbox
        self.word_count_spinbox = tk.Spinbox(self.main_frame, from_=3, to=24, state="readonly")
        self.word_count_spinbox.grid(row=0, column=1, padx=(5, 20), pady=10, sticky=tk.E)

        # "Generate Passphrase" button
        self.generate_button = tk.Button(self.main_frame, text="Generate Passphrase", command=self.generate_passphrase)
        self.generate_button.grid(row=1, column=0, padx=(20, 5), pady=10, columnspan=1, sticky=tk.W)

        # "Copy to Clipboard" button
        self.copy_button = tk.Button(self.main_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=1, column=1, padx=(5, 20), pady=10, columnspan=1, sticky=tk.E)

        self.passphrase_var = tk.StringVar()
        self.passphrase_var.set("")

        self.passphrase_display = tk.Label(self.main_frame, textvariable=self.passphrase_var, wraplength=500)
        self.passphrase_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Center the button
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

    def generate_passphrase(self):
        word_count = int(self.word_count_spinbox.get())
        with open('words_alpha.txt', 'r') as f:
            words = [line.strip() for line in f]
        passphrase = '-'.join(secrets.choice(words) for _ in range(word_count))
        self.passphrase_var.set(passphrase)

        # Calculate the width based on the length of the passphrase text
        text_width = self.passphrase_display.winfo_reqwidth()

        # Calculate the desired window width with some padding
        window_width = text_width + 50

        self.master.geometry(f"{window_width}x180")

    def copy_to_clipboard(self):
        # Copy the passphrase to the clipboard
        passphrase = self.passphrase_var.get()
        pyperclip.copy(passphrase)

        # Show a pop-up message
        messagebox.showinfo("Copied!", "Passphrase copied to clipboard!")

def main():
    root = tk.Tk()
    app = PassphraseGenerator(root)
    root.geometry("300x145")  # Set initial size
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
