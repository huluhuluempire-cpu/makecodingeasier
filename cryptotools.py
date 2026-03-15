

def generate_key_file():
    key = Fernet.generate_key()
    myfile = open("key.txt", "wb")
    myfile.write(key)
    myfile.close()

def encrypt_file_contents(file_name, key):
    contents = ""
    myfile = open(file_name, "r")
    contents = myfile.read()
    myfile.close()
    
    encrypted_content = key.encrypt(contents.encode())
    
    
    newfile = open(file_name, "wb")
    newfile.write(encrypted_content)
    newfile.close()
    

def decrypt_file_contents(file_name, key):
    contents=""
    myfile = open(file_name, "rb")
    contents = myfile.read()
    myfile.close()
    
    decrypted_content = key.decrypt(contents)
    
    newfile = open(file_name, "w")
    newfile.write(decrypted_content.decode())
    newfile.close()

def encrypt_folder(folder_path, key):
    files = os.listdir(folder_path)

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            encrypt_file_contents(full_path, key)

def decrypt_folder(folder_path, key):
    files = os.listdir(folder_path)

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            decrypt_file_contents(full_path, key)
    
    
    
    
