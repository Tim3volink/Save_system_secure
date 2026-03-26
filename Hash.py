class Hash:
    def __init__(self, data):
        self.data = data

    def hashing(self):
        h = 0
        for char in self.data:            
            h = (h * 1009 + ord(char)) % 1000000007
        return str(h)
    
    def data_hash(self):
        final = self.data + '|' + self.hashing()
        return final
    
    def returning(self, hash_only = False):
        if not hash_only:
            return self.data_hash()
        else:
            return self.hashing()