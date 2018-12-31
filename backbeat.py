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
	print("Requests module is required")
	exit()
try:  # For waiting
	import time
except:
	print("Time module is required")
	exit()
try: # For file dialog
	from tkinter import filedialog
	from tkinter import *
except:
	print("tkinter.filedialog is required")
	exit()
# Create a blank dictionary
complete = []
# Open the CSV
filecsv = Tk()
filecsv.filename = filedialog.askopenfilename(initialdir = "~/",title = "Select csv file to open",filetypes = (("CSV files","*.csv"),("all files","*.*")))
print ("Opening file " + filecsv.filename)
# Start work on the CSV file
with open(filecsv.filename, 'r') as f: # Open the file
	worklist = csv.DictReader(f)
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
	fieldnames = ['Source','Destination','Status','History','EndUrl']
	with open(csvname,'w') as s: #Save the file
		w = csv.DictWriter(s, fieldnames = fieldnames)
		w.writeheader()
		for k in complete:
			w.writerow(k)
		print("Saved CSV")
else:
	print("Okay we're done here.")
# Here endeth the lessen
print("The end")
exit()
