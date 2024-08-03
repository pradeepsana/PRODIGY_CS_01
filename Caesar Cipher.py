def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? (or 'q' to quit): ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice, please try again.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        elif choice == 'd':
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
