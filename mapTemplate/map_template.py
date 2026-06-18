import os

import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

BASE_URL = "https://URL/api/v1.3"
TEMPLATE_NAME = "MP-EXAMPLE"

CLUSTER_IDS = [
    "10.33.233.200",
    "10.33.233.201",
]

encoding = os.getenv("AUTH_TOKEN")

headers = {
    "Authorization": f"Basic {encoding}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}

rules = [
    (
        "10.20.38.0",
        "255.255.255.0",
        "1719..1720",
        "CM 10.20.38.0/24 port range 1719-1720",
    ),
    (
        "10.20.38.0",
        "255.255.255.0",
        "5060",
        "CM 10.20.38.0/24 port 5060",
    ),
    (
        "10.20.38.0",
        "255.255.255.0",
        "52233",
        "CM 10.20.38.0/24 port 52233",
    ),
    (
        "10.20.46.0",
        "255.255.255.0",
        "1719..1720",
        "CM 10.20.46.0/24 port range 1719-1720",
    ),
    (
        "10.20.46.0",
        "255.255.255.0",
        "5060",
        "CM 10.20.46.0/24 port 5060",
    ),
    (
        "10.20.46.0",
        "255.255.255.0",
        "52233",
        "CM 10.20.46.0/24 port 52233",
    ),
]


def port_match(port):
    if ".." in port:
        start, end = port.split("..")

        return {
            "type": "portDst",
            "pos": 0,
            "value": int(start),
            "valueMax": int(end),
            "subset": "none",
        }

    return {
        "type": "portDst",
        "pos": 0,
        "value": int(port),
        "subset": "none",
    }


def build_pass_rules():
    pass_rules = []

    for rule_id, item in enumerate(rules, start=1):
        ip, mask, port, comment = item

        pass_rules.append(
            {
                "ruleId": rule_id,
                "comment": comment,
                "bidi": True,
                "matches": [
                    {
                        "type": "ipVer",
                        "pos": 0,
                        "value": "v4",
                    },
                    {
                        "type": "ip4Dst",
                        "pos": 0,
                        "value": ip,
                        "netMask": mask,
                    },
                    port_match(port),
                ],
            }
        )

    return pass_rules


def check_response(response, action):
    print(f"{action}: HTTP {response.status_code}")

    if response.status_code not in [200, 201, 202, 204]:
        print(response.text)
        response.raise_for_status()


def create_template(cluster_id):
    url = f"{BASE_URL}/mapTemplates?clusterId={cluster_id}"

    payload = {
        "alias": TEMPLATE_NAME,
        "comment": "Template example",
        "rules": {
            "passRules": build_pass_rules(),
            "dropRules": [],
        },
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        verify=False,
    )

    check_response(
        response,
        f"Creating template {TEMPLATE_NAME} on cluster {cluster_id}",
    )


def save_config(cluster_id):
    url = f"{BASE_URL}/config/save?clusterId={cluster_id}"

    response = requests.post(
        url,
        headers=headers,
        verify=False,
    )

    check_response(
        response,
        f"Saving configuration on cluster {cluster_id}",
    )


def main():
    if not encoding:
        raise RuntimeError("AUTH_TOKEN was not found in the .env file")

    for cluster_id in CLUSTER_IDS:
        print(f"\n=== Processing cluster {cluster_id} ===")

        create_template(cluster_id)
        save_config(cluster_id)

    print("\nCompleted successfully.")


if __name__ == "__main__":
    main()
