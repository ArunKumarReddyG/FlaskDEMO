import requests
import json

BASE= "http://127.0.0.1:5000/"

headers= {'Content-type':'application/json'}


res= requests.get(BASE + "mtask/101", headers = {"Content-Type": "application/json"})
print(res)

