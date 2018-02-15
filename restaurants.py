import pymongo

connection = pymongo.MongoClient('homer.stuy.edu')
db = connection['test']
collection = db['restaurants']

def find_borough(borough):
    cursor = collection.find({'borough': borough})
    print 'RESTAURANTS IN ' + borough + ':\n'
    i = 0
    for result in cursor:
        print result['name']
        i += 1
    print str(i) + ' found'

def find_zip(zipcode):
    cursor = collection.find({'address.zipcode': zipcode})
    print 'RESTAURANTS IN ' + zipcode + ':\n'
    i = 0
    for result in cursor:
        print result['name']
        i += 1
    print str(i) + ' found'

def find_zip_and_grade(zipcode,grade):
    cursor = collection.find({'address.zipcode': zipcode , 'grades.grade' : grade})
    print 'RESTAURANTS IN ' + zipcode + ' WITH A GRADE OF ' + str(grade) + ':\n'
    i = 0
    for result in cursor:
        print result['name']
        i += 1
    print str(i) + ' found'

def find_zip_and_maxscore(zipcode,score):
    cursor = collection.find({'address.zipcode': zipcode , 'grades.score' : {'$lt' : score}})
    print 'RESTAURANTS IN ' + zipcode + ' WITH A SCORE LESS THAN ' + str(score) + ':\n'
    i = 0
    for result in cursor:
        print result['name']
        i+=1
    print str(i) + ' found'

def find_zip_and_cuisine(zipcode,cuisine):
    cursor = collection.find({'address.zipcode': zipcode , 'cuisine' : cuisine})
    print 'RESTAURANTS IN ' + zipcode + ' WITH ' + str(cuisine) + ' CUISINE:\n'
    i = 0
    for result in cursor:
        print result['name']
        i+=1
    print str(i) + ' found'

find_borough('Brooklyn')
print '\n\n\n\n'
find_zip('11209')
print '\n\n\n\n'
find_zip_and_grade('11209','A')
print '\n\n\n\n'
find_zip_and_maxscore('11209',5)
print '\n\n\n\n'
find_zip_and_cuisine('11209','Middle Eastern')
