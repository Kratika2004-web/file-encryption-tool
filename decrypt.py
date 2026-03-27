from cryptography.fernet import Fernet

# Load the key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)

# Open encrypted file
with open("encrypted_sample.txt", "rb") as enc_file:
    encrypted = enc_file.read()

# Decrypt the data
decrypted = fernet.decrypt(encrypted)

# Save decrypted file
with open("decrypted_sample.txt", "wb") as dec_file:
    dec_file.write(decrypted)

print("File Decrypted Successfully!")