# Import tkinter module
import tkinter as tk

# Import the other python files
import gui_check_strongpass
import gui_password_generator
import gui_user_storage
import gui_encryption

# Create a root window
root = tk.Tk()
root.title("Password Tool")

# Create a label for the title
title_label = tk.Label(root, text="Welcome to the Password Tool")
title_label.grid(row=0, columnspan=2, padx=10, pady=10)

# Define the function to open the password generator file
def open_password_generator():
    # Close the root window
    root.destroy()
    
    # Run the password generator file
    gui_password_generator.main()

# Define the function to open the password checker file
def open_password_checker():
    # Close the root window
    root.destroy()
    
    # Run the password checker file
    gui_check_strongpass.main()

# Define the function for User Storage button
def user_storage():
    print("User Storage button clicked")
    root.destroy()
    gui_user_storage.main()

# Define the function for Encrypt/Decrypt File button
def encrypt_decrypt_file():
    print("Encrypt/Decrypt File button clicked")
    root.destroy()
    gui_encryption.main()

# Create a button for the password generator option
generator_button = tk.Button(root, text="Password Generator", command=open_password_generator)
generator_button.grid(row=1, column=0, padx=10, pady=10)

# Create a button for the password checker option
checker_button = tk.Button(root, text="Password Checker", command=open_password_checker)
checker_button.grid(row=1, column=1, padx=10, pady=10)

# Create a button for User Storage option
user_storage_button = tk.Button(root, text="User Storage", command=user_storage)
user_storage_button.grid(row=2, column=0, padx=10, pady=10)

# Create a button for Encrypt/Decrypt File option
encrypt_decrypt_file_button = tk.Button(root, text="Encrypt/Decrypt File", command=encrypt_decrypt_file)
encrypt_decrypt_file_button.grid(row=2, column=1, padx=10, pady=10)

# Start the main loop of the root window
root.mainloop()
