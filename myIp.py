#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account
from decouple import config

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = config("SHEET_ID")


while True:


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

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()


        # opening and reading the file
        file_read = open("request.txt", "r")

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
            # Getting last ip and datetime
            oldFile = open("myip.json", "r")
            oldDict = json.load(oldFile)
            oldFile.close()
	    # Getting the day time and the Ip to write to JSON file
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            lineLen = len(new_list)
          # If Ip has changed save the time it changed
            v = new_list[0].find(":")
            v += 2
            ip = new_list[0][v:-4]
            if (oldDict["myIp"] == ip):
                data = {"myIp": ip, "dtOfChange": oldDict["dtOfChange"]}
                myIp = open("myip.json", "w")
                json.dump(data, myIp)
                myIp.close()
                print("Ip didn't change. Ip: " + ip + " Hour: " + oldDict["dtOfChange"])
            else:
                data2 = {"myIp": ip, "dtOfChange": dt_string}
                myIp2 = open("myip.json", "w")
                json.dump(data2, myIp2)
                myIp2.close()
                print("Ip Changed. Ip: " + ip + " Hour: " + dt_string)
                bodyValue2 = [[dt_string, ip]]
                request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range="IpHist!A:B",
                                    valueInputOption="USER_ENTERED",
                                    body={"values": bodyValue2}).execute()
 # entering except block
# if input file doesn't exist
    except :
        print("\nThe file doesn't exist!")
