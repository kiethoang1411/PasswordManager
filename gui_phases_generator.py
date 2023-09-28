from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import base64
import os
import tkinter as tk
from tkinter import filedialog, simpledialog

class RSAEncryption:
    def __init__(self, key_file='rsa_key.pem'):
        self.key_file = key_file
        self.password = simpledialog.askstring("Password", "Enter password:", show='*')
        salt = b'\x00'*16  # Should be a random value in a real application
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        self.key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))

        try:
            with open(self.key_file, 'rb') as f:
                encrypted_key = f.read()
            fernet = Fernet(self.key)
            decrypted_key = fernet.decrypt(encrypted_key)
            self.rsa_key = serialization.load_pem_private_key(decrypted_key, password=None, backend=default_backend())
        except FileNotFoundError:
            self.rsa_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
            pem = self.rsa_key.private_bytes(encoding=serialization.Encoding.PEM,
                                             format=serialization.PrivateFormat.PKCS8,
                                             encryption_algorithm=serialization.NoEncryption())
            fernet = Fernet(self.key)
            encrypted_key = fernet.encrypt(pem)
            with open(self.key_file, 'wb') as f:
                f.write(encrypted_key)

        self.cipher = PKCS1_OAEP.new(self.rsa_key)

    def encrypt_file(self, filename):
        with open(filename, 'r') as f:
            message = f.read()
        encrypted_message = self.cipher.encrypt(message.encode())
        destination = filedialog.asksaveasfilename(defaultextension='.enc')
        with open(destination, 'w') as f:
            f.write(base64.b64encode(encrypted_message).decode())

    def decrypt_file(self, filename):
        with open(filename, 'r') as f:
            encrypted_message = base64.b64decode(f.read().encode())
        decrypted_message = self.cipher.decrypt(encrypted_message)
        destination = filedialog.asksaveasfilename(defaultextension='.dec')
        with open(destination, 'w') as f:
            f.write(decrypted_message.decode())

def user_interface():
    rsa = RSAEncryption()
    root = tk.Tk()
    root.title("Encrypt File")  # Set the window title here
    root.geometry("200x100")  # Set the window size here
    root.resizable(False, False)  # Disable resizing

    def choose_file():
        filename = filedialog.askopenfilename()
        return filename

    def encrypt():
        filename = choose_file()
        rsa.encrypt_file(filename)

    def decrypt():
        filename = choose_file()
        rsa.decrypt_file(filename)

    encrypt_button = tk.Button(root, text="Encrypt a file", command=encrypt)
    decrypt_button = tk.Button(root, text="Decrypt a file", command=decrypt)

    encrypt_button.pack()
    decrypt_button.pack()

    root.mainloop()

# Run the user interface
user_interface()
