from bs4 import BeautifulSoup
import requests

html = requests.get("http://192.168.15.1/webClient/index.html").content

soup = BeautifulSoup(html, 'html.parser')

f = open("request.txt", "w")
f.write(str(soup))
f.close()

file_name = "request.txt"

# using try catch except to
# handle file not found error.

# entering try block
try:

    # opening and reading the file
    file_read = open(file_name, "r")

    # asking the user to enter the string to be
    # searched
    text = "liWanIp"

    # reading file content line by line.
    lines = file_read.readlines()

    new_list = []
    idx = 0

    # looping through each line in the file
    for line in lines:

        # if line have the input string, get the index
        # of that line and put the
        # line into newly created list
        if text in line:
            new_list.insert(idx, line)
            idx += 1
    # closing file after reading
    file_read.close()

    # if length of new list is 0 that means
    # the input string doesn't
    # found in the text file
    if len(new_list)==0:
        print("\n\"" +text+ "\" is not found in \"" +file_name+ "\"!")
    else:

        # displaying the lines
        # containing given string
        lineLen = len(new_list)
        print("\n**** Lines containing \"" +text+ "\" ****\n")
        cleanIp = open("myIp.txt", "w")
        cleanIp.write("")
        cleanIp.close()
        myIp = open("myIp.txt", "a")
        v = new_list[0].find(":")
        v += 2
        myIp.write(new_list[0][v:-4])
        myIp.close()




# entering except block
# if input file doesn't exist
except :
    print("\nThe file doesn't exist!")

