import requests
import hashlib
import tkinter as tk

class PasswordChecker:
    def __init__(self, root):
        self.root = root
        root.title("Have I Been Pwned?")

        # Create a label
        self.label = tk.Label(root, text="Enter the password to check:")
        self.label.pack(pady=10)

        # Create an entry widget for password input
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack(pady=5)

        # Create a button to check the password
        self.check_button = tk.Button(root, text="Check Password", command=self.check_password)
        self.check_button.pack(pady=10)

        # Create a label to display the result
        self.result_label = tk.Label(root, text="", font=("bold", 12))
        self.result_label.pack()

    def get_hash_prefix(self, password):
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        return sha1_hash[:5]

    def check_password_pwned(self, password):
        # Get the first 5 characters of the hash
        hash_prefix = self.get_hash_prefix(password)

        # Make a GET request to the "Have I Been Pwned" API
        api_url = f"https://api.pwnedpasswords.com/range/{hash_prefix}"
        response = requests.get(api_url)

        # Check if the response status code is OK (200)
        if response.status_code == 200:
            # Split the response by line and check if the full hash appears
            hashes = response.text.split('\n')
            full_hash = hashlib.sha1(password.encode()).hexdigest().upper()[5:]
            for h in hashes:
                if h.startswith(full_hash):
                    return f"The password has been pwned {h.split(':')[1]} times."
            return "The password has not been pwned."
        else:
            return "Failed to check the password."

    def check_password(self):
        password = self.password_entry.get()
        result = self.check_password_pwned(password)
        
        if "not been pwned" in result:
            self.result_label.config(text=result, fg="blue")
        else:
            self.result_label.config(text=result, fg="red")


def main():
    # Create the main window
    root = tk.Tk()
    app = PasswordChecker(root)
    root.geometry("300x180")
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
