# pomeranian image generator

with open("secrets/bingsecrets.txt") as f:
    secrets = f.readlines()
account_key = secrets[0].rstrip('\n')

import urllib
import requests
from requests.auth import HTTPBasicAuth
import json
import random

def get_pom():
    """ this function's sole purpose is to amass images of pomeranian pups! """

    # search url obtained from bing api
    url = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q=pomeranian&count=1000&offset=0&mkt=en-us&safeSearch=Moderate"

    # get ~authorized~
    headers = {'Ocp-Apim-Subscription-Key': account_key}

    # get response from search url
    response_data = requests.get(url, headers=headers)

    # decode json-formatted response & save as pomeranians.json
    json_result = response_data.json()
    json_pretty = json.dumps(json_result, indent=4, sort_keys=True)
    with open("pomeranians.json","w") as outfile:
        outfile.write(json_pretty)
    outfile.close()

    # generate & download random images (one at a time) from pomeranians.json
    i = random.randrange(0,150)
    img_url = json_result['value'][i]['thumbnailUrl']
    print img_url
    if json_result['value'][i]['encodingFormat'] == "jpeg":
        img_path = "img/" + str(i) + ".jpg"
    else:
        img_path = "img/" + str(i) + ".png"
    urllib.urlretrieve(img_url, img_path)

    return "complete!"
