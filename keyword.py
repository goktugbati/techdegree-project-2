import string
from collections import OrderedDict

from ciphers import Cipher

class Keyword(Cipher):
    alphabet = string.ascii_uppercase

    def __init__(self, keyword = 'keyword'):
        """Initilizes the class with the uppercase alphabet"""
        self.keyword = keyword

    def encrypt(self, text):
        """Encrypts the given text by changing the index of each
        letter in the text"""
        output = []
        text = text.upper()
        new_alphabet = self.create_keyword_alphabet(self.keyword)
        #Iterates over each letter and finds the corresponding letter
        #in the new alphabet
        for char in text:
            try:
                index = self.alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(new_alphabet[index])
        return ''.join(output)

    def decrypt(self, text):
        """Decyrpts the given text by changing the index of each
        letter in the text"""
        output = []
        text = text.upper()
        new_alphabet = self.create_keyword_alphabet(self.keyword)
        #Iterates over each letter and finds the corresponding letter
        #in the ascii_uppercase alphabet
        for char in text:
            try:
                index = new_alphabet.index(char)
            except ValueError:
                output.append(char)
            else:
                output.append(self.alphabet[index])
        return ''.join(output)


    @staticmethod
    def create_keyword_alphabet(keyword):
        """Creates the new alphabet needed for encryption by adding
           the given Keyword to the beginning of the alphabet and removing
           the duplicates"""
        alphabet = "".join(OrderedDict.fromkeys(keyword.upper() + string.ascii_uppercase))
        return alphabet

# kw_1 = Keyword('keyword')
# encrypted_message = kw_1.encrypt('Paintball is super fun')
# decyrypted_message = kw_1.decrypt(encrypted_message)
# print(encrypted_message)
# print(decyrypted_message)
