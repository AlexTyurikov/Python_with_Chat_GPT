def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                # Сдвиг для строчных букв
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                # Сдвиг для прописных букв
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text.append(new_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Пример использования
text_to_encrypt = input('Введите шифрования: ')

print('Текст для шифрования:', text_to_encrypt)

shift_value = int(input('Введите сдвиг: '))

encrypted_text = caesar_encrypt(text_to_encrypt, shift_value)
print(f"Encrypted: {encrypted_text}")  # При сдвиге 3 для "Hello world! - вывод: "Khoor, Zruog!"

decrypted_text = caesar_decrypt(encrypted_text, shift_value)
print(f"Decrypted: {decrypted_text}")  # Для "Khoor, Zruog!" - вывод: "Hello, World!"