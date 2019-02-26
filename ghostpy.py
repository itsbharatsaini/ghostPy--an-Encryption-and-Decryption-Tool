from encrypting_file import encryption
from decrypting_file import decryption
from print import print_logo

print_logo()
while True:
    option = None
    print('''
Choose an Option...
        
[1]-->Encryption
[2]-->Decryption
        ''')
    try:
        option = int(input('''Enter Your Choose ==> '''))
    except:
        print("\nInput Should Be a Integer.")
    if option == 1:
        encryption()
    elif option == 2:
        decryption()
    else:
        print("\nChoose Correct Option.")
        print("Please Try again...")