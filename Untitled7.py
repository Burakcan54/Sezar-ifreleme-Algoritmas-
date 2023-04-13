#!/usr/bin/env python
# coding: utf-8

# In[5]:


class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        # Şifrelemek için kullanılacak anahtarın değerini alın
        key = self.key
        # Şifrelenecek metni büyük harflere dönüştür
        plaintext = plaintext.upper()
        # Şifreli metin için boş bir dize oluştur
        ciphertext = ''
        # Her karakteri kaydırarak şifreli metni oluştur
        for char in plaintext:
            if char.isalpha():
                char_idx = ord(char) - ord('A')
                shifted_idx = (char_idx + key) % 26
                ciphertext += chr(shifted_idx + ord('A'))
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        # Şifre çözmek için kullanılacak anahtarın değerini alın
        key = self.key
        # Şifreli metni büyük harflere dönüştür
        ciphertext = ciphertext.upper()
        # Deşifrelenmiş metin için boş bir dize oluştur
        plaintext = ''
        # Her karakteri kaydırarak deşifrelenmiş metni oluştur
        for char in ciphertext:
            if char.isalpha():
                char_idx = ord(char) - ord('A')
                shifted_idx = (char_idx - key) % 26
                plaintext += chr(shifted_idx + ord('A'))
            else:
                plaintext += char
        return plaintext

# Örnek kullanım
plaintext = input("Lütfen şifrelenecek metni girin: ")
key = int(input("Lütfen anahtar değerini girin: "))
cipher = CaesarCipher(key)
ciphertext = cipher.encrypt(plaintext)
print("Şifrelenmiş metin: ", ciphertext)
decryptedtext = cipher.decrypt(ciphertext)
print("Deşifrelenmiş metin: ", decryptedtext)


# In[ ]:




