import os

file1 = open("myIp.txt", "r")
file2 = open("newIp.txt", "r")
if str(file1.read()) != str(file2.read()):
    file2.close()
    file3 = open("newIp.txt", "w")
    file3.write(file1.read())
    file1.close()
    file3.close()
else:
    file1.close()
    file2.close()
