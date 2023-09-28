import os
import base64
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class SecureRSA:
    def __init__(self):
        self.rsa_key = None

    def generate_key(self):
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

    def load_key(self):
        f = filedialog.askopenfile(mode='rb', filetypes=[('PEM', '*.pem')])
        if f is None:  # askopenfile return `None` if dialog closed with "cancel".
            return
        pem = f.read()
        f.close()
        self.rsa_key = serialization.load_pem_private_key(pem, password=None)

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
        decrypted_message = self.rsa_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        destination = filedialog.asksaveasfilename(defaultextension='.dec')
        with open(destination, 'w') as f:
            f.write(decrypted_message.decode())

def user_interface():
    secure_rsa = SecureRSA()
    root = tk.Tk()
    root.title("File Encryption/Decryption")  
    root.geometry("250x150")  
    root.resizable(False, False)  

    def generate_key():
        secure_rsa.generate_key()

    def load_key():
        secure_rsa.load_key()

    def choose_file():
        filename = filedialog.askopenfilename()
        return filename

    def encrypt():
        filename = choose_file()
        secure_rsa.encrypt_file(filename)

    def decrypt():
        filename = choose_file()
        secure_rsa.decrypt_file(filename)

    generate_button = tk.Button(root, text="Generate Key", command=generate_key)
    load_button = tk.Button(root, text="Load Key", command=load_key)
    encrypt_button = tk.Button(root, text="Encrypt a file", command=encrypt)
    decrypt_button = tk.Button(root, text="Decrypt a file", command=decrypt)

    generate_button.pack()
    load_button.pack()
    encrypt_button.pack()
    decrypt_button.pack()

    root.mainloop()

user_interface()
