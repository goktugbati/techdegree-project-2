from ciphers import Cipher

class Transposition(Cipher):
    """This class implements RAIL FENCE cipher as a form of
    Transposition cipher"""
    def __init__(self, key):
        """Initilizes the class"""
        self.key = key

    def encrypt(self, text):
        """Encrypts the given """
        result = ""
        #Create a matrix len(text) x key
        matrix = [["" for i in range(len(text))] for y in range(self.key)]
        count_column = 0
        count_row = 0
        increment = 1
        for char in text:
            if count_row + increment < 0 or count_row + increment == len(matrix):
                increment *= -1
            matrix[ count_row ][ count_column ] = char
            count_row += increment
            count_column += 1

        count_row = 0
        count_column = 0
        while count_row != self.key:
             for i in range(len(text)):
                 if(matrix[count_row][i] != ""):
                     result += matrix[count_row][i]
             count_row += 1
        return result

    def decrypt(self, text):
        result = ""
        matrix = [["" for i in range(len(text))] for y in range(self.key)]
        count_row = 0
        index = 0
        index2 = 0
        for i in range(self.key):
            for y in range(len(text)):
                if(index < len(text)):
                    print(count_row)
                    matrix[i][index] = text[index2]
                    index += self.key+1
                    index2 += 1
            index = i + 1
        return matrix


trans_1 = Transposition(3)
encrypted_message = trans_1.encrypt('Paintball is super fun')
decyrypted_message = trans_1.decrypt('Ptl euanbl ssprfniaiu')
print(encrypted_message)
print(decyrypted_message)
