from Hash import *
from Cryptage import *

my_data = "level:1;niveau:1"
crypt = Cryptage(Hash(my_data).returning()).encrypte()
print(crypt)
open("test.dat", "w").write(crypt)