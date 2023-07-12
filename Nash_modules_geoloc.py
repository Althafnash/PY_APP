import requests
import json

def geo():
    print()
    ip_address = input("Enter an ip adress :) :  \n" )
    request_url = 'https://geolocation-db.com/jsonp/' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = result.split("(")[1].strip(")")
    result  = json.loads(result)
    print("\n")
    print(result)

geo()