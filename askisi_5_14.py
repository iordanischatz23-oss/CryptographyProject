import requests
from datetime import datetime

def print_bitcoin_time_block(x):
    url = f'https://blockchain.info/block-height/'+str(x)+'?format=json'
    
    r = requests.get(url)
    data = r.json()
    time = data['blocks'][0]['time']
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# Εκτύπωση των πρώτων 5 blocks (0 έως 4)
for i in range(5):
    print(f"Block {i+1}: {print_bitcoin_time_block(i)}")