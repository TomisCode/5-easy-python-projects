from cryptography.fernet import Fernet
message = "I want to keep this a secret"
key = b"wGwHGg7CFyPyFjX_Vemj4MS3suPa6VGQilZrqlX1Li8="

fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
decMessage = fernet.decrypt(encMessage).decode()

print("Original : " + message)
print("Encrypted : " + str(encMessage))
print("Decrypted : " + str(decMessage))

key = Fernet.generate_key()
print("Your key is: ".ljust(10), key.rjust(30))
