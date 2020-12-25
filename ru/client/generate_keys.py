from cryptography.fernet import Fernet

key = Fernet.generate_key()
key2 = Fernet.generate_key()

with open('key1.txt', 'w', encoding='utf-8') as f:
    f.write(key.decode())

with open('key2.txt', 'w', encoding='utf-8') as f2:
    f2.write(key2.decode())
