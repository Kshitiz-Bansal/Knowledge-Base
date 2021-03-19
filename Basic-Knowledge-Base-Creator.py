# Knowledge Base Assignment

# Kshitiz Bansal, 2019CS50438

# How to run?
# create a folder by name "assignment_knowledge_base" in same directory as this file 
# then run
# it creates .txt and .csv files of individual ppl 
# and files "master.csv" and "master.txt" which contain the required knowledge base 


# What did I learn?
# --> What are knowledge bases and how are they used?
# --> What is web scraping?
# --> How search engines work
# --> Using regular expressions
# --> How regular expressions work using deterministic finite automata

import requests 
import csv
from bs4 import BeautifulSoup 
import re # regex 
  
BASE_URL = "https://en.wikipedia.org/w/index.php?title="
FILENAME = "Person_"
master = []
all_ppl = ["Joe_Biden", 
			"Barack_Obama", 
			"Donald_Trump", 
			"Hillary_Clinton", 
			"Jesse_Ventura", 
			"George_W._Bush", 
			"Bill_Clinton", 
			"George_H._W._Bush", 
			"Ronald_Reagan", 
			"Jimmy_Carter", 
			"Gerald_Ford", 
			"Richard_Nixon"]
for person in all_ppl:
	individual = []
	URL = BASE_URL + person + "&action=edit"
	r = requests.get(URL) 
	  
	soup = BeautifulSoup(r.content, 'html5lib')

	table = soup.find('textarea', attrs = {'id':'wpTextbox1', 'accesskey':',', 'name':'wpTextbox1', 'class':'mw-editfont-monospace', 'cols':'80', 'rows':'25'})
	# print(table.text)
	data = str(table)
	data = data[:3500] # all required info appears in the first 5000 chars, reached 5000 by trial and error
	# print(data)
	pattern = re.compile(r'\s(?=| )(?=\w+\s+(?== ))')
	result = re.split(pattern, data)
	result = result[4:]
	for row in result:
		try:
			split_row = row.split(' = ')
			predicate = split_row[0].strip()
			val = split_row[1].strip()
			val = val.replace("((", " ")
			val = val.replace("))", " ")
			val = val.replace("[[", " ")
			val = val.replace("]]", " ")
			val = val.replace("{{", " ")
			val = val.replace("}}", " ")
			val = val.strip()
			val = val[:-2]
			master.append([person, predicate, val])
			individual.append([person, predicate, val])
		except:
			pass
	# print(*master, sep="\n")
	with open("assignment_knowledge_base/{}_{}.csv".format(FILENAME, person), 'w', newline='') as f:
		w = csv.writer(f, ['Name', 'Predicate', 'Object'])
		w.writerow(['Name', 'Predicate', 'Object'])
		print('writing csv file of ' + person)
		for info in individual:
			try:
				w.writerow(info)
			except:
				pass

	with open("assignment_knowledge_base/{}_{}.txt".format(FILENAME, person), 'w', newline='') as f:
		w = csv.writer(f, ['Name', 'Predicate', 'Object'])
		w.writerow(['Name', 'Predicate', 'Object'])
		print('writing txt file of ' + person)
		for info in individual:
			try:
				w.writerow(info)
			except:
				pass


with open("assignment_knowledge_base/master.csv", 'w', newline='') as f:
		w = csv.writer(f, ['Name', 'Predicate', 'Object'])
		w.writerow(['Name', 'Predicate', 'Object'])
		print("writing final csv file")
		for info in master:
			try:
				w.writerow(info)
			except:
				pass				

with open("assignment_knowledge_base/master.txt", 'w', newline='') as f:
		w = csv.writer(f, ['Name', 'Predicate', 'Object'])
		w.writerow(['Name', 'Predicate', 'Object'])
		print("writing final txt file")
		for info in master:
			try:
				w.writerow(info)
			except:
				pass				
