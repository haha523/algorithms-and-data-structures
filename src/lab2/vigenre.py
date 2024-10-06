def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()  
    keyword_length = len(keyword)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():  
            shift = ord(keyword[i % keyword_length]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char 
    
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword = keyword.upper()  
    keyword_length = len(keyword) 
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():  
            shift = ord(keyword[i % keyword_length]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            elif char.islower():
                plaintext += chr((ord(char) - ord('a') - shift + 26) % 26 + ord('a'))
        else:
            plaintext += char  
    
    return plaintext

plaintext = input("Простой текст: ")
keyword = input("Ключ: ")
ciphertext = encrypt_vigenere(plaintext, keyword)
print("Зашифрованный текст: " , ciphertext)  

decrypted_text = decrypt_vigenere(ciphertext, keyword)
print("Декодируется текст: " , decrypted_text)  
