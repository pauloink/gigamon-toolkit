import os
import requests
from dotenv import load_dotenv
from tabulate import tabulate

rows = []

load_dotenv()

base_url = "https://URL/api/v1.3"

encoding = os.getenv('AUTH_TOKEN')

headers = {
    'Authorization':  f'Basic {encoding}',
    'Accept': 'application/json'
}

node = '/nodes'
nodes = base_url + node

url = requests.get(nodes, headers=headers, verify=False)

data = url.json()

for cluster in data.get("clusters", []):
    for member in cluster.get("members", []):
        rows.append([
            member.get("hostname"),
            member.get("deviceIp"),
            member.get("model"),
            member.get("serialNumber"),
            member.get("swVersion"),
        ])

print(tabulate(
    rows,
    headers=['Hostname', 'IP', 'Model', 'Serial', 'Version'],
    tablefmt='grid'
))

