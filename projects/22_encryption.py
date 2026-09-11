def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter a message: ")
shift = int(input("Enter a shift value: "))

encrypted_message = encrypt(message, shift)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt(encrypted_message, shift)
print(f"Decrypted message: {decrypted_message}")