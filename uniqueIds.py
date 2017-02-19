import sys
import pymongo
from pymongo import MongoClient
from pprint import pprint
import datetime
#Default File Path
connection = MongoClient('localhost', 27017)
db = connection['GEDCOMDB']
def check_distinct_individual(id):
	individual_list = db.people.distinct('_id',{"ID" : id})
	if len(individual_list) == 1:
		return "true"
	else:
		return "false"

def main(n):
    individual_list = check_distinct_individual(n)
    print(individual_list)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(str(sys.argv[1]))

