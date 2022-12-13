import requests
import json
import sqlite3
import pandas as pd

#creation of the database 
#Connecting to sqlite
conn = sqlite3.connect('btc_blocks.db')

#Creating a cursor object using the cursor() method
c = conn.cursor()

#Create a table blocks with columns like height, timestamp, bits,nonce, hashrate,prev_block_hash,next_block_hash,size,difficulty,reward_block,confirmations,weight
#c.execute(''' CREATE TABLE Blocks (height INT, timestamp INT, bits INT,nonce INT , hashrate INT ,prev_block_hash INT,next_block_hash INT,size INT,difficulty INT,reward_block INT,confirmations INT,weight INT) ''')

#Commit your changes in the database
#conn.commit()

url_latest_block='https://chain.api.btc.com/v3/block/latest'

#get the height of the latest block mined
response_api_latest_block_mined=requests.get(url_latest_block)
height_latest_block_mined=response_api_latest_block_mined.json()['data']['height']


url_specific_block='https://chain.api.btc.com/v3/block/759'

def get_block_information(url):
    
    response_api=requests.get(url_specific_block)#Fetch data from chain api
    #print(response_api.status_code)#give 200 is it was able the response is good
    #print(response_api.json())#see the data in json format

    height=response_api.json()['data']['height']
    timestamp=response_api.json()['data']['timestamp']
    bits=response_api.json()['data']['bits']
    nonce=response_api.json()['data']['nonce']
    hashrate=response_api.json()['data']['hash']
    prev_block_hash=response_api.json()['data']['prev_block_hash']
    next_block_hash=response_api.json()['data']['next_block_hash']
    size=response_api.json()['data']['size']
    difficulty=response_api.json()['data']['difficulty']
    reward_block=response_api.json()['data']['reward_block']
    reward_fees=response_api.json()['data']['reward_fees']
    confirmations=response_api.json()['data']['confirmations']
    weight=response_api.json()['data']['weight']

    #Put the data fetching into the database
    c.execute('''INSERT INTO Blocks VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (height, timestamp, bits,nonce, hashrate,prev_block_hash,next_block_hash,size,difficulty,reward_block,confirmations,weight))
    return

#get_block_information(url_specific_block)

#Commit your changes in the database
#conn.commit()
#print('complete')

c.execute('''SELECT * FROM Blocks''')
results=c.fetchall()
#print(results)

df=pd.read_sql_query('''SELECT * FROM Blocks''', conn)
print(df)
conn.close()

"""#Select data into the database



res=c.fetchall()
print(res)
#print(height, timestamp, bits,nonce, hashrate,prev_block_hash,next_block_hash,size,difficulty,reward_block,confirmations,weight)
#Doping EMPLOYEE table if already exists
c.execute("DROP TABLE Height")
print("Table dropped... ")

#Commit your changes in the database
conn.commit()
"""