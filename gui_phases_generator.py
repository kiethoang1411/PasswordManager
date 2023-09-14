import tkinter as tk
from tkinter import messagebox
import secrets
import string

class PassphraseGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Passphrase Generator")

        self.word_count_label = tk.Label(self.master, text="Number of words:")
        self.word_count_label.pack(padx=10, pady=10)

        self.word_count_spinbox = tk.Spinbox(self.master, from_=3, to=24, state="readonly")
        self.word_count_spinbox.pack(padx=10, pady=10)

        self.generate_button = tk.Button(self.master, text="Generate Passphrase", command=self.generate_passphrase)
        self.generate_button.pack(padx=10, pady=10)

        self.passphrase_var = tk.StringVar()
        self.passphrase_var.set("")

        self.passphrase_display = tk.Label(self.master, textvariable=self.passphrase_var)
        self.passphrase_display.pack(padx=10, pady=10)

    def generate_passphrase(self):
        word_count = int(self.word_count_spinbox.get())
        with open('words_alpha.txt', 'r') as f:
            words = [line.strip() for line in f]
        passphrase = '-'.join(secrets.choice(words) for _ in range(word_count))
        self.passphrase_var.set(passphrase)

def main():
    root = tk.Tk()
    app = PassphraseGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
