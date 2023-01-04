import pymongo

#creaing a database
#To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and the name of the database you want to create.
# MongoDB will create the database if it does not exist, and make a connection to it.
# Important: In MongoDB, a database is not created until it gets content!
# MongoDB waits until you have created a collection (table), with at least one document (record) before it actually creates the database (and collection).
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]


#Return a list of your system's databases
print(myclient.list_database_names())


#Check if "mydatabase" exists:
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
  
  
# A collection in MongoDB is the same as a table in SQL databases.
#Creating a Collection
# To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
# MongoDB will create the collection if it does not exist.
#Create a collection called "customers":
mycol = mydb["customers"]


#Important: In MongoDB, a collection is not created until it gets content!
#MongoDB waits until you have inserted a document before it actually creates the collection
#You can check if a collection exist in a database by listing all collections:
print(mydb.list_collection_names())#Return a list of all collections in your database:


#check a specific collection by name:
#Check if the "customers" collection exists:
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")


#Insert Document
#A document in MongoDB is the same as a record in SQL databases.
#To insert a record, or document as it is called in MongoDB, into a collection, we use the insert_one() method.
#The first parameter of the insert_one() method is a dictionary containing the name(s) and value(s) of each field in the document you want to insert."""
mydict = { "name": "John", "address": "Highway 37" }


#The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.
#x = mycol.insert_one(mydict)#Return the _id Field
#print(x.inserted_id)
#If you do not specify an _id field, then MongoDB will add one for you and assign a unique id for each document.
# In the example above no _id field was specified, so MongoDB assigned a unique _id for the record (document).


#mydict1={"name":"Grace", "address":"340 Avenue de la capelette"}
#mycol.insert_one(mydict1)

#Insert Multiple Documents
#To insert multiple documents into a collection in MongoDB, we use the insert_many() method.
#the first parameter of the insert_many() method is a list containing dictionaries with the data you want to insert:
"""
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
"""

#Insert Multiple Documents, with Specified IDs
#If you do not want MongoDB to assign unique ids for you document, you can specify the _id field when you insert the document(s).
#Remember that the values has to be unique. Two documents cannot have the same _id.

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 3, "name": "Amy", "address": "Apple st 652"},
  { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "_id": 5, "name": "Michael", "address": "Valley 345"},
  { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "_id": 8, "name": "Richard", "address": "Sky st 331"},
  { "_id": 9, "name": "Susan", "address": "One way 98"},
  { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "_id": 12, "name": "William", "address": "Central st 954"},
  { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)