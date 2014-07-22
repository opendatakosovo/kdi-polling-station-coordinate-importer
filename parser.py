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
			lat = row[4]
			lon = row[5]
			
			stationNumber=row[6]
			print(stationNumber + ': ' + lat + ' - ' + lon)
			cursor = collection.find({'pollingStation.number':stationNumber})
	
			if cursor.count() == 0:
				print("not matched " + stationNumber)
			elif cursor.count() == 1:
				
				doc_id=cursor[0]['_id']
				collection.update({'_id':doc_id},{'$set':{'pollingStation.coordinates':{'lat':lat,'lon':lon}}})
				print(cursor[0]['_id'])
				
			else:
				print("Error: Multiple Match")

result()



