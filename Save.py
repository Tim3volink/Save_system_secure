from Hash import *
from Cryptage import *

class Save:
    def __init__(self, data):
        self.data = data
        self.saved_write = open("save.dat", "w")

    def crypted_data(self):
        text_hash = Hash(self.data).returning()
        text_crypt = Cryptage(text_hash).encrypte()
        return str(text_crypt)
    
    def save(self):
        self.saved_write.write(self.crypted_data())