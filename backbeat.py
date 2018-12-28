# -*- coding: utf-8 -*-

# A 404 link checker

try: # For importing the CSV module
	import csv
except:
	print("CSV module is required")
	exit()
try:  # For getting the URL response
	import requests
except:
	print("requests is required")
	exit()
try:  # For waiting
	import time
except:
	print("time is required")
	exit()
try:  # For saving as CSV
	import pandas
except:
	print("pandas is required")
	exit()
try: # For the save as option
	from tkinter import filedialog
	from tkinter import *
except:
	print("tkinter.filedialog is required")
	exit()
# Open the CSV
filecsv = Tk()
filecsv.filename = filedialog.askopenfilename(initialdir = "~/",title = "Select csv file to open",filetypes = (("CSV files","*.csv"),("all files","*.*")))
print ("Opening file " + filecsv.filename)

# Start work on the CSV file
worklist = csv.DictReader(open(filecsv.filename, 'r'))
complete = []
for row in worklist:
	print("Working on " + row['Destination'])
	line = {}
	try:
		page = requests.head(row['Destination'],allow_redirects=True,timeout=5)
		line = dict(
			Source = row['Source'],
			Destination = row['Destination'],
			Status = page.status_code,
			History = page.history,
			EndUrl = page.url
		)
		complete.append(line)
	except:
		print("Url error for " + row['Destination'])
		line = dict(
			Source = row['Source'],
			Destination = row['Destination'],
			Status = 'ERROR',
			History = '',
			EndUrl = ''
		)
		complete.append(line)
print(complete)
# See if we want to save the file
dosave = input("Do you want to save a CSV — Type 'Y' for yes or anything else for no. ")
if dosave == 'Y' or dosave =='y': #If we're saving let's save
	file_name = filedialog.asksaveasfilename()
	#Attempt to create a CSV
	csvname = file_name + '.csv'
	pandas.DataFrame(complete).to_csv(csvname, index=False)
	print("Saved CSV")
else:
	print("Okay we're done here.")
# Here endeth the lessen
print("The end")
exit()
