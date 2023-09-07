# Import tkinter module
import tkinter as tk

class PasswordStrengthChecker:
    # Define the constructor method
    def __init__(self, master):
        # Set the master window
        self.master = master
        self.master.title("Password Strength Checker")

        # Create a label for the password entry
        self.password_label = tk.Label(self.master, text="Enter your password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a password entry widget
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create a label for the password strength
        self.strength_label = tk.Label(self.master, text="Password strength:")
        self.strength_label.grid(row=1, column=0, padx=10, pady=10)

        # Create a variable to store the password strength
        self.strength_var = tk.StringVar()
        self.strength_var.set("")

        # Create a label to display the password strength
        self.strength_display = tk.Label(self.master, textvariable=self.strength_var)
        self.strength_display.grid(row=1, column=1, padx=10, pady=10)

        # Create a canvas to draw the colored line
        self.line_canvas = tk.Canvas(self.master, width=200, height=20)
        self.line_canvas.grid(row=2, columnspan=2, padx=10, pady=10)

        # Bind the entry widget to the update_strength method 
        self.password_entry.bind("<KeyRelease>", self.update_strength)

    # Define the method to check the password strength
    def check_password_strength(self, password: str) -> int:
        # Set initial password strength to 0
        strength = 0
        length_password = False
        
        # Check password length
        if len(password) < 8:
            return strength
        
        if len(password) >= 14:
            length_password = True
        
        # Check for lowercase letters
        has_lowercase = any(char.islower() for char in password)
        
        # Check for uppercase letters
        has_uppercase = any(char.isupper() for char in password)
        
        # Check for digits
        has_digits = any(char.isdigit() for char in password)
        
        # Check for special characters
        has_special = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>/?' for char in password)

        # Check for spaces
        has_spaces = any(char.isspace() for char in password)
        
        # Update strength based on criteria
        if has_lowercase or has_uppercase:
            strength = 1    # extremely weak
        if (has_lowercase and has_digits) or (has_uppercase and has_digits):
            strength = 2    # weak
        if has_lowercase and has_uppercase and has_digits:
            strength = 3    # medium       
        if has_lowercase and has_uppercase and has_digits and has_special:
            strength = 4    # strong
        if has_lowercase and has_uppercase and has_digits and has_special and length_password:
            strength = 5    # very strong
        if has_lowercase and has_uppercase and has_digits and has_special and has_spaces:
            strength = 5    # very strong
        if has_lowercase and has_uppercase and has_digits and has_special and length_password and has_spaces:
            strength = 6    # extremely strong
            
        return strength

    # Define the method to update the password strength display
    def update_strength(self, event):
        # Get the password from the entry widget
        password = self.password_entry.get()
        
        # Check the password strength using the method code
        strength = self.check_password_strength(password)
        
        # Set the corresponding text for the strength variable
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
        
        # Clear the canvas 
        self.line_canvas.delete("all")
        
        # Draw the colored line on the canvas 
        self.line_canvas.create_line(0, 10, line_length, 10, fill=line_color, width=10)

# Define a main function
def main():
    root = tk.Tk()
    app = PasswordStrengthChecker(root)
    root.mainloop()

# Check if the script is executed as the main program
if __name__ == "__main__":
    main()