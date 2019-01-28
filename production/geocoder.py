import requests

# Example: API_KEY = 'AIzaSyC9azed9tLdjpZNjg2_kVePWvMIBq154eA'
# Key1: AIzaSyBLtMUM-8vNSGkFDsYJGLgX1YIDJjVHneg
# Key2: AIzaSyD3fFgQDRXPfxaF8lauzkUnpJdBQNXUeWg
# Key3: AIzaSyCpAT2eUeP4U2iwgsOmN1xNqldugmLNVaw
# Key4: AIzaSyCmuk_aDUtHZQs0B2dXLlzKtJCtWAwp6co
API_KEY = 'AIzaSyBLCtTQMxFgPiqSIK5DY-tatZr72ExeCqw'

http_proxy = "http://localhost:5555"
https_proxy = "https://localhost:5555"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy
            }

def geocode_url(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json?address={}".format(address)
    geocode_url = geocode_url + "&key={}".format(API_KEY)
    return geocode_url

def geocode_address(address):
    url = geocode_url(address)
    results = requests.get(url, proxies=None)
    results = results.json()
    answer = results['results'][0]
    output = {
        "latitude": answer.get('geometry').get('location').get('lat'),
        "longitude": answer.get('geometry').get('location').get('lng')
    }
    return output
