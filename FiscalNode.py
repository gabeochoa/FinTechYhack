from keys import fiscalnotekey
import requests
import json
from FNBill import FNBill
from collections import namedtuple

apik = '&apikey=' + fiscalnotekey
url='https://api.fiscalnote.com/bills?q=taxi+private'+apik

response = requests.get(url)
data = response.json()
#a = FNBill(data)

client = FiscalNoteClient(fiscalnotekey)
client.legislators(q='john', )

print(data)
#print(a.data[0])

