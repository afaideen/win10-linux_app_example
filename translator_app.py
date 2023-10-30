import requests, uuid, json

# Add your key and endpoint
# key = "a491739135d844bb8b90851ffa8cac5a"
key = "fa919f130b94438793527aae71782499"
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastasia"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    # 'from': 'en',
    'to': ['fr', 'es', 'ar', 'tr', 'ms', 'en', 'nb', 'de', 'ru', 'ja', 'it', ]
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    # 'text': 'I would really like to drive your car around the block a few times!'
    # 'text': "J’aimerais vraiment conduire votre voiture autour du pâté de maisons plusieurs fois!"
    'text': "Jeg vil veldig gjerne kjøre bilen rundt kvartalet et par ganger!"
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))