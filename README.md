# MakeCodeEasier 🛠️

**MakeCodeEasier** is a simple Python library to make common file operations easier.  
It wraps **cryptography** and **os** functionality into easy-to-use functions for:

- File encryption and decryption
- Folder batch encryption and decryption
- Key generation for Fernet encryption

---

## Features

- `generate_key_file()` – Creates a key file
- `encrypt_file_contents(file_name, key)` – Encrypt a single file
- `decrypt_file_contents(file_name, key)` – Decrypt a single file
- `encrypt_folder(folder_path, key)` – Encrypt all files in a folder
- `decrypt_folder(folder_path, key)` – Decrypt all files in a folder

---

## Installation (via GitHub)

```bash
pip install git+https://github.com/huluhuluempire-cpu/makecodeeasier.git
