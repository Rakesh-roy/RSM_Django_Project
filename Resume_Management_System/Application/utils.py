import requests
import json
import os


def sendOtpText(message, contact):
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "cLN4VEhwvyFYDSarJsk7jIWbq35HtmofnUGiXZROQxd1TlMp92g1WOL0o4lsM26rhe5YqZvKQfz8kaDH", "sender_id": "FSTSMS", "message": message,
                   "language": "english", "route": "p", "numbers": contact}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = response.text
    data = json.loads(json_data)
    return data['return']
