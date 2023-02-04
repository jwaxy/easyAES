from hashlib import sha256
from pyaes import AESModeOfOperationCBC
from base64 import b64encode, b64decode
from secrets import token_bytes

class AES(object):
    def __init__(self, key):
        self.block_size = 16
        self.key = sha256(key.encode()).digest()

    """Encrypts a string and base64 encodes it."""
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = token_bytes(self.block_size)
        cipher = AESModeOfOperationCBC(self.key, iv = iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

    """Decrypts a base64 encoded and crypted string."""
    def decrypt(self, encrypted_text):
        encrypted_text = b64decode(encrypted_text)
        iv = encrypted_text[:self.block_size]
        cipher = AESModeOfOperationCBC(self.key, iv = iv)
        plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
        return self.__unpad(plain_text)

    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text

    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]
