import csv

from pymongo import MongoClient
from bson import ObjectId

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.kdi
collection = db.localelectionsfirstround2013

def result():

	with open('qendrat_votimit.csv', 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			stationNumber=row[6]
			cursor = collection.find({'pollingStation.number':stationNumber})
	
			if cursor.count() == 0:
				print("not matched " + stationNumber)
			elif cursor.count() == 1:
				print(cursor[0]['pollingStation'])
				
			else:
				print("Error: Multiple Match")

result()
