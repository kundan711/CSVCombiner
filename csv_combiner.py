import email
import json
import os
import sys
import csv
from venv import create
import pandas as pd

#Combines multiple CSV file and adds an extra column to give the file name it was extracted from
class CSVCombiner():

    #Main function to retrieve the file name and concat the output CSV file
    def main (self, mode = 'normal'):
        argumentlist = []
        if(mode == 'unittest'):
            argumentlist=["./fixtures/clothing.csv", "./fixtures/accessories.csv"]
        else:
            if(len(sys.argv) < 2):
                print("Missing command-line argument")
                return ("Missing command-line argument")
            argumentlist = sys.argv[1:]
        alldata = pd.DataFrame()
        for file in argumentlist:
            fileCheck = self.checkFile(file)
            if(fileCheck):
                df = self.readFile(file)
                alldata = pd.concat([alldata, df])
        csv_data = (alldata.to_csv(index=False, lineterminator='\n', sep='|'))
        if(mode == 'normal'):
            print(csv_data)
        else:
            return csv_data

    #Function to read indivdual CSV file and extract the data in to data frame
    def readFile(self, file):
        df = pd.read_csv(file)
        df.columns = map(str.lower, df.columns)
        filenametemp = file.split("/")[2]
        email_hash=[]
        category=[]
        filename = []
        for index, row in df.iterrows():
            try:
                email_hash.append(row['email_hash'])
                category.append(row['category'])
                filename.append(filenametemp)
            except:
                pass
        d = {'email_hash': email_hash, 'category': category, 'filename': filename}
        dataf = pd.DataFrame(data=d)
        return dataf
        
    #Function to validate the File    
    def checkFile(self, file):
        if(len(file) <= 1):
            print("No file path provided")
            return False

        if (not os.path.exists(file)):
            print("File not found")
            return False

        filename = file.split("/")[2]
        if(len(filename.split(".")) < 2 or filename.split(".")[1] !="csv"):
            print("not a CSV file")
            return False

        if (os.path.getsize(file) == 0):
            print("File is empty")
            return False
        return True             

if __name__ == '__main__':
    obj = CSVCombiner()
    obj.main()