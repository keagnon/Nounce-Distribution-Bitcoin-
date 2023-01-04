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
#c.execute(''' CREATE TABLE Blocks (height INT, timestamp INT, bits INT,nonce INT , hashrate INT ,prev_block_hash INT,next_block_hash INT,size INT,difficulty INT,reward_block INT,confirmations INT,weight INT) ''')
#Commit your changes in the database
#conn.commit()

url_latest_block='https://chain.api.btc.com/v3/block/latest'

#get the height of the latest block mined
response_api_latest_block_mined=requests.get(url_latest_block)
height_latest_block_mined=response_api_latest_block_mined.json()['data']['height']

def get_block_information(url):
    
    response_api=requests.get(url)#Fetch data from chain api
    #print(response_api.status_code)#give 200 is it was able the response is good
    #print(response_api.json())#see the data in json format

    height=response_api.json()['data']['height']
    version_block=response_api.json()['data']['version']
    mrkl_root_block=response_api.json()['data']['mrkl_root']
    timestamp=response_api.json()['data']['timestamp']
    bits=response_api.json()['data']['bits']
    nonce=response_api.json()['data']['nonce']
    hashrate=response_api.json()['data']['hash']
    prev_block_hash=response_api.json()['data']['prev_block_hash']
    next_block_hash=response_api.json()['data']['next_block_hash']
    size=response_api.json()['data']['size']
    pool_difficulty=response_api.json()['data']['pool_difficulty']
    difficulty=response_api.json()['data']['difficulty']
    difficulty_double=response_api.json()['data']['difficulty_double']
    tx_count=response_api.json()['data']['tx_count']
    reward_block=response_api.json()['data']['reward_block']
    reward_fees=response_api.json()['data']['reward_fees']
    confirmations=response_api.json()['data']['confirmations']
    is_orphan=response_api.json()['data']['is_orphan']
    curr_max_timestamp=response_api.json()['data']['curr_max_timestamp']
    is_sw_block=response_api.json()['data']['is_sw_block']
    stripped_size=response_api.json()['data']['stripped_size']
    sigops=response_api.json()['data']['sigops']
    weight=response_api.json()['data']['weight']
   # message=response_api.json()['data']['message']
    #status=response_api.json()['data']['status']

    #Put the data fetching into the database
    #c.execute('''INSERT INTO Blocks VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (height,version_block,mrkl_root_block, timestamp, bits,nonce, hashrate,prev_block_hash,next_block_hash,size,pool_difficulty,difficulty,difficulty_double,tx_count,reward_block,reward_fees,confirmations,is_orphan,curr_max_timestamp,is_sw_block,stripped_size,sigops,weight,message,status))
    #c.execute('''INSERT INTO Blocks VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', (height, timestamp, bits,nonce, hashrate,prev_block_hash,next_block_hash,size,difficulty,reward_block,confirmations,weight))
    return

def get_all_urls():
    #on crée une liste pour mettre les urls
    urls=[]
    latest=51
    
    for i in range(10):
        url1=f"https://chain.api.btc.com/v3/block/{i}"
        urls.append(url1)
        get_block_information(url=url1)
        #print(i)
        
        
get_all_urls()
conn.commit()
#Commit your changes in the database
df=pd.read_sql_query('''SELECT * FROM Blocks''', conn)
print(df)
conn.close()

