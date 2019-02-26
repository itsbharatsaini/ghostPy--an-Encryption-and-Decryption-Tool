import base64
import getpass
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
def decryption():
    print("\nWelcome to gostpy Decryption Tool...!!\n")

    def decrypt_file():
        input_file = files_path
        with open(input_file, 'rb') as f:
            data = f.read()
        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(data)
        with open(input_file, 'wb') as f:
            f.write(decrypted_data)
        print("File '" + input_file + "' is Decrypted.")

    def decrypt_folder():
        for root, dirs, files in os.walk(files_path):
            folder_path = root
            for file_name in files:
                input_file = folder_path + '\\' + file_name
                with open(input_file, 'rb') as f:
                    data = f.read()
                fernet = Fernet(key)
                try:
                    decrypted_data = fernet.decrypt(data)
                    with open(input_file, 'wb') as f:
                        f.write(decrypted_data)
                    print("File '" + input_file + "' is Decrypted.")
                except:
                    print("File '" + input_file + "' is Not Decrypted.")

    password_provided = input("Enter Your Encrypted File Password : ")
    if len(password_provided) < 1:
        print("Please Provide Password")
    else:
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
        files_path = input("Drag and Drop your file or folder here : ")
        print("Files are Decrypting ... ")
        file_name = os.path.isfile(files_path)
        if file_name == True:
            decrypt_file()
        else:
            decrypt_folder()