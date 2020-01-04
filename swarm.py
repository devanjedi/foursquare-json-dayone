#!/usr/local/bin/python3

import json
from datetime import datetime

with open("checkins.json", "r") as read_file:
    data = json.load(read_file)

for entry in data['items']:
    ts = entry['createdAt']
    dt = datetime.fromtimestamp(ts)
    print("Date: "+dt.strftime("%b %d, %Y at %I:%M:%S %p %z EDT" + "\n\n"))
    if entry['venue']:
        venue=entry['venue']
        print("Visited "+venue['name'])
        print("URL: "+venue['url'])
        print("\n\n\n\n")
