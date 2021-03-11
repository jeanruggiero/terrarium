import os
import requests

TOKEN = os.environ.get("DNSIMPLE_API_TOKEN")
ACCOUNT_ID = os.environ.get("DNSIMPLE_ACCOUNT_ID")
ZONE_ID = "highlift.io"
RECORD_ID = "22634373"

# Get current IP
IP = requests.get("http://icanhazip.com/").text

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Accept': 'application/json'
}

data = {
    'content': IP
}

# Update DNS record with current IP
requests.patch(f"https://api.dnsimple.com/v2/{ACCOUNT_ID}/zones/{ZONE_ID}/records/{RECORD_ID}", headers=headers,
               data=data)

