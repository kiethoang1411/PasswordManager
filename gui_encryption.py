import os
import base64
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class SecureRSA:
    def __init__(self, root):
        self.root = root
        self.rsa_key = None
        self.top_frame = tk.Frame(root)  # Create a frame at the top of the window
        self.top_frame.pack(side='top', fill='x')
        self.key_status = tk.Label(self.top_frame, text="Key is not loaded", fg="red")  # Create the label in the frame
        self.key_status.pack(side='left')  # Pack the label to the left of the frame
        self.create_widgets()

    def create_widgets(self):
        def generate_key():
            self.rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            pem = self.rsa_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            f = filedialog.asksaveasfile(mode='wb', defaultextension=".pem")
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            f.write(pem)
            f.close()

        def load_key():
            f = filedialog.askopenfile(mode='rb', filetypes=[('PEM', '*.pem')])
            if f is None:  # askopenfile return `None` if dialog closed with "cancel".
                return
            pem = f.read()
            f.close()
            self.rsa_key = serialization.load_pem_private_key(pem, password=None)
            self.key_status.config(text="Key is loaded", fg="blue")  # Change the label text and color when a key is loaded
        
        def generate_key():
            self.rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
            pem = self.rsa_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
            f = filedialog.asksaveasfile(mode='wb', defaultextension=".pem")
            if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
                return
            f.write(pem)
            f.close()
            self.key_status.config(text="Key is loaded", fg="blue")  # Change the label text and color when a key is generated

        def choose_file(is_decrypt=False):
                if is_decrypt:  # If we are decrypting, filter for .enc files
                    filename = filedialog.askopenfilename(filetypes=[('Encrypted Files', '*.enc')])
                else:  # Otherwise, filter for .txt files
                    filename = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
                return filename

        def encrypt():
            filename = choose_file()
            if filename is not None:
                self.encrypt_file(filename)

        def decrypt():
            filename = choose_file(is_decrypt=True)
            if filename is not None:
                self.decrypt_file(filename)

        def how_to_use():  # New function to show instructions
            instructions = """
            1. Generate or Load a Key: Click on 'Generate Key' to create a new RSA key or 'Load Key' to use an existing one.
            
            2. Choose a .txt File: Click on 'Encrypt a file' or 'Decrypt a file' and select the .txt file you want to process.
            
            3. Encrypt or Decrypt the File: The app will use the loaded RSA key to encrypt or decrypt the selected .txt file.
            
            4. Exit: Click on 'Exit' when you're done.
            """
            messagebox.showinfo("How to Use", instructions)
            
        def exit_button():
            self.root.destroy()

        generate_button = tk.Button(self.root, text="Generate Key", command=generate_key)
        generate_button.pack()

        load_button = tk.Button(self.root, text="Load Key", command=load_key)
        load_button.pack()

        encrypt_button = tk.Button(self.root, text="Encrypt a file", command=encrypt)
        encrypt_button.pack()

        decrypt_button = tk.Button(self.root, text="Decrypt a file", command=decrypt)
        decrypt_button.pack()

        how_to_use_button = tk.Button(self.root, text="How to Use", command=how_to_use, width=10)  # New How to Use button
        how_to_use_button.pack(side='left', padx=10)  # Pack the How to Use button to the right
        
        exit_button = tk.Button(self.root, text="Exit", command=exit_button, width=10)
        exit_button.pack(side='right', padx=10, pady=10)

    def encrypt_file(self, filename):
        if self.rsa_key is None:
            messagebox.showerror("Error", "RSA key is not set. Please generate or load a key before encrypting.")
            return
        with open(filename, 'r') as f:
            message = f.read()
        encrypted_message = self.rsa_key.public_key().encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        destination = filedialog.asksaveasfilename(defaultextension='.enc')
        with open(destination, 'wb') as f:
            f.write(base64.b64encode(encrypted_message))

    def decrypt_file(self, filename):
        if self.rsa_key is None:
            messagebox.showerror("Error", "RSA key is not set. Please generate or load a key before decrypting.")
            return
        with open(filename, 'rb') as f:
            encrypted_message = base64.b64decode(f.read())
        try:
            decrypted_message = self.rsa_key.decrypt(
                encrypted_message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except ValueError:
            messagebox.showerror("Error", "Decryption failed. The file may not have been encrypted with the loaded key.")
            return
        destination = filedialog.asksaveasfilename(defaultextension='.txt')
        if destination:  # Check if a file name was entered
            with open(destination, 'w') as f:
                f.write(decrypted_message.decode())



def main():
    root = tk.Tk()
    root.title("Encrypt/Decrypt File")
    root.geometry("300x180")
    root.resizable(False, False)
    app = SecureRSA(root)
    root.mainloop()

if __name__ == "__main__":
    main()
