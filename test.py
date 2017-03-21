import json
import csv
import sys

f = open("test.csv","w")
w = csv.writer(f)
row=[]
reload(sys)
sys.setdefaultencoding('utf-8')
with open('test.json') as json_data:
	d=json.load(json_data)
	for key in d:
		row.append(key)
		w.writerow(row)
		del row[:]

	f.close()
