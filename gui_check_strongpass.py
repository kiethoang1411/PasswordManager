import tkinter as tk
from tkinter import messagebox
import re

class PasswordStrengthChecker:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Strength Checker")

        self.common_topologies = ["Ullllldd", "Ulllllldd", "Ullldddd", "Ullllllldd", "Ulllldddd", 
                                  "Ulllllll", "Ulllllld", "UlllSlll", "UlllllddS", "UdSllllll",
                                  "Sddllll", "UddlllS", "lSllldddS", "UddSddll", "UdSllllllld",
                                  "SddllllddS", "UddlllSdd", "UddlllSdd", "ldddSllld",
                                  "UllllSddSll"]
        
        self.common_label = tk.Label(self.master, text="Common Pattern:")
        self.common_label.grid(row=4, column=0, padx=10, pady=10)

        self.common_var = tk.StringVar()
        self.common_var.set("")

        self.common_display = tk.Label(self.master, textvariable=self.common_var)
        self.common_display.grid(row=4, column=1, padx=10, pady=10)

        self.password_label = tk.Label(self.master, text="Enter your password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        self.strength_label = tk.Label(self.master, text="Password strength:")
        self.strength_label.grid(row=1, column=0, padx=10, pady=10)

        self.strength_var = tk.StringVar()
        self.strength_var.set("")

        self.strength_display = tk.Label(self.master, textvariable=self.strength_var)
        self.strength_display.grid(row=1, column=1, padx=10, pady=10)

        self.pattern_label = tk.Label(self.master, text="Password pattern:")
        self.pattern_label.grid(row=2, column=0, padx=10, pady=10)

        self.pattern_var = tk.StringVar()
        self.pattern_var.set("")

        self.pattern_display = tk.Label(self.master, textvariable=self.pattern_var)
        self.pattern_display.grid(row=2, column=1, padx=10, pady=10)

        self.line_canvas = tk.Canvas(self.master, width=200, height=20)
        self.line_canvas.grid(row=3, columnspan=2, padx=10, pady=10)

        self.pattern_label = tk.Label(self.master, text="Password pattern:")
        self.pattern_label.grid(row=2, column=0, padx=10, pady=10)

        self.pattern_info_button = tk.Button(self.master, text="?", command=self.show_pattern_info)
        self.pattern_info_button.grid(row=2, column=2, padx=10, pady=10)

        self.password_entry.bind("<KeyRelease>", self.update_strength)

    def show_pattern_info(self):
       messagebox.showinfo("Pattern Information", """Password topology defines how a password is constructed in terms of character types and their arrangement. Hacker can use some common topologies to break your password.
                           \n\nU = uppercase\nl = lowercase\nd = digit\nS = special character""")

    def check_password_strength(self, password):
        strength = 0
        length_password = False

        if len(password) < 8:
            return strength

        if len(password) >= 14:
            length_password = True

        has_lowercase = any(char.islower() for char in password)
        has_uppercase = any(char.isupper() for char in password)
        has_digits = any(char.isdigit() for char in password)
        has_special = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>/?' for char in password)
        has_spaces = any(char.isspace() for char in password)

        if has_lowercase or has_uppercase:
            strength = 1
        if (has_lowercase and has_digits) or (has_uppercase and has_digits):
            strength = 2
        if has_lowercase and has_uppercase and has_digits:
            strength = 3
        if has_lowercase and has_uppercase and has_digits and has_special:
            strength = 4
        if has_lowercase and has_uppercase and has_digits and has_special and length_password:
            strength = 5
        if has_lowercase and has_uppercase and has_digits and has_special and has_spaces:
            strength = 5
        if has_lowercase and has_uppercase and has_digits and has_special and length_password and has_spaces:
            strength = 6

        return strength
    
    def check_common_topology(self, pattern):
        return pattern in self.common_topologies

    def analyze_password_pattern(self, password):
        pattern = ""
        for char in password:
            if char.isupper():
                pattern += "U"
            elif char.islower():
                pattern += "l"
            elif char.isdigit():
                pattern += "d"
            else:
                pattern += "S"

        if self.check_common_topology(pattern):
            self.common_var.set("Yes")
        else:
            self.common_var.set("No")

        return pattern

    def update_strength(self, event):
        password = self.password_entry.get()
        strength = self.check_password_strength(password)
        pattern = self.analyze_password_pattern(password)

        if strength == 0:
            self.strength_var.set("Too short")
            line_color = "red"
            line_length = 0
        elif strength == 1:
            self.strength_var.set("Extremely weak")
            line_color = "red"
            line_length = 40
        elif strength == 2:
            self.strength_var.set("Weak")
            line_color = "orange"
            line_length = 80
        elif strength == 3:
            self.strength_var.set("Medium")
            line_color = "yellow"
            line_length = 120
        elif strength == 4:
            self.strength_var.set("Strong")
            line_color = "green"
            line_length = 160
        elif strength == 5:
            self.strength_var.set("Very strong")
            line_color = "blue"
            line_length = 200
        elif strength == 6:
            self.strength_var.set("Extremely strong")
            line_color = "purple"
            line_length = 200

        self.pattern_var.set(pattern)
        self.line_canvas.delete("all")
        self.line_canvas.create_line(0, 10, line_length, 10, fill=line_color, width=10)

def main():
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
