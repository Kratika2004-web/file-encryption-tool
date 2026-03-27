from cryptography.fernet import Fernet

# Generate a key and save it
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Open the file to encrypt
with open("sample.txt", "rb") as file:
    original = file.read()

# Encrypt the data
encrypted = fernet.encrypt(original)

# Save encrypted file
with open("encrypted_sample.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)

print("File Encrypted Successfully!")