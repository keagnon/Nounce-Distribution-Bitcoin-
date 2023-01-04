import pymongo
import requests
import json

#creating database
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
db=myclient["btc_list_block"]

#creating a collection called blocks
collection1=db["blocks"]

#Delete all documents in a collection
#x = collection1.delete_many({})


url_latest_block='https://chain.api.btc.com/v3/block/latest'
#get the height of the latest block mined
response_api_latest_block_mined=requests.get(url_latest_block)
height_latest_block_mined=response_api_latest_block_mined.json()['data']['height']


def get_block_information(url):
    
    #Fetch data from chain api
    response_api=requests.get(url)
    
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
    message=response_api.json()['message']
    status=response_api.json()['status']
    err_code=response_api.json()['err_code']
    err_no=response_api.json()['err_no']
    pool_name=response_api.json()['data']['extras']['pool_name']
    pool_link=response_api.json()['data']['extras']['pool_link']
    
    document_collection={ "_id": height, "height": height, "version_block": version_block,"mrkl_root":mrkl_root_block,"timestamp":timestamp,"bits":bits,"nonce":nonce,"hashrate":hashrate,"prev_block_hash":prev_block_hash,"next_block_hash":next_block_hash,"size":size,"pool_difficulty":pool_difficulty,"difficulty":difficulty,"difficulty_double":difficulty_double,"tx_count":tx_count,"reward_block":reward_block,"reward_fees":reward_fees,"confirmations":confirmations,"is_orphan":is_orphan,"curr_max_timestamp":curr_max_timestamp,"is_sw_block":is_sw_block,"stripped_size":stripped_size,"sigops":sigops,"weight":weight,"message":message,"status":status,"err_code":err_code,"err_no":err_no,"pool_name":pool_name,"pool_link":pool_link}
    x=collection1.insert_one(document_collection)
    print(x.inserted_id)
    

    """print(height)
    print(version_block)
    print(mrkl_root_block)
    print(timestamp)
    print(bits)
    print(nonce)
    print(hashrate)
    print(prev_block_hash,next_block_hash,sigops,size,pool_difficulty,difficulty,difficulty_double)
    print(tx_count,reward_block,reward_fees,confirmations,is_orphan,curr_max_timestamp)
    print(is_sw_block,stripped_size,weight,message,status,err_code,err_no,pool_link,pool_name)"""
    return


def get_all_urls():
    #on crée une liste pour mettre les urls
    urls=[]
    latest=height_latest_block_mined + 1
    
    for i in range(282818, latest):
        url1=f"https://chain.api.btc.com/v3/block/{i}"
        urls.append(url1)
        get_block_information(url=url1)
        print(f"collecting data from {url1}")
        
        
get_all_urls()
