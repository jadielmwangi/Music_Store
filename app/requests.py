import urllib.request,json
import requests


#USER_AGENT = 'default-007'
#headers = {
    #'user-agent': 'default-007'
#}

#API_KEY='db4de38368557995c224c9cca508843f'
#def configure_request(app):
    #global api_key,base_url
    #api_key=app.config['API_KEY']
# Getting api key
#api_key = app.config['API_KEY']

# Getting the base url
#base_url = app.config["API_BASE_URL"]
#payload = {
    #'api_key': API_KEY,
    #'method': 'chart.gettopartists',
    #'format': 'json'
#}

#def lastfm_get(app):
    # define headers and URL
#    headers = {'user-agent': USER_AGENT}
#    url = 'http://ws.audioscrobbler.com/2.0/default-007/'

    # Add API key and format to the payload
 #   payload['api_key'] = API_KEY
#    payload['format'] = 'json'
#
#    response = requests.get(url, headers=headers, params=payload)
 #   return response

#r = lastfm_get({
#    'method': 'chart.gettopartists'
#})

#print(r.json())

def get_quotes():

    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes = response.json()

    return quotes