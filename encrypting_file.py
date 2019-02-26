import base64
import getpass
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def encryption():
    print("\nWelcome to gostpy Encryption Tool...!!\n")
    def take_password():
        password_provided = input('Choose  Password :')
        if len(password_provided) < 1:
            print("Please Provide Password")
        else:
            reconfirm_password = input("Confirm  Password : ")
            if len(reconfirm_password) < 1:
                print("Please Provide Password")
        return (password_provided, reconfirm_password)

    def encrypt_file():
        input_file = files_path
        with open(input_file, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        with open(input_file, 'wb') as f:
            f.write(encrypted_data)
        print("File '" + files_path + "' is Encrypted.")

    def encrypt_folder():
        for root, dirs, files in os.walk(files_path):
            folder_path = root
            for file_name in files:
                input_file = folder_path + '\\' + file_name
                with open(input_file, 'rb') as f:
                    data = f.read()
                fernet = Fernet(key)
                encrypted_data = fernet.encrypt(data)
                with open(input_file, 'wb') as f:
                    f.write(encrypted_data)
                print("File '" + input_file + "' is Encrypted.")

    password_provided, reconfirm_password = take_password()
    if password_provided == reconfirm_password:
        password = password_provided.encode()
        salt = b'ghostpy'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))

        files_path = input("\nDrag and Drop your file or folder here : ")
        print("Files are Encrypting ... ")

        file_name = os.path.isfile(files_path)
        if file_name == True:
            encrypt_file()
        else:
            encrypt_folder()
    else:
        print("\nPassword Not Match")
        print("Try Again...!!")

