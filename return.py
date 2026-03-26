from Hash import *

hashed = open("test.dat").read()
decoded = ""
for i in range(len(hashed)):
    decoded += hashed[i]

data, h = decoded.split('|')

if Hash(data).returning(True) == h:
    print(True)
else:
    print(False)