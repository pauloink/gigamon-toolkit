import os

import requests
import urllib3
from dotenv import load_dotenv
from tabulate import tabulate

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

BASE_URL = "https://URL/api/v1.3"
AUTH_TOKEN = os.getenv("AUTH_TOKEN")


def get_inventory():
    if not AUTH_TOKEN:
        raise RuntimeError("AUTH_TOKEN was not found in the .env file")

    headers = {
        "Authorization": f"Basic {AUTH_TOKEN}",
        "Accept": "application/json",
    }

    response = requests.get(
        f"{BASE_URL}/nodes",
        headers=headers,
        verify=False,
        timeout=30,
    )

    response.raise_for_status()
    data = response.json()

    rows = []

    for cluster in data.get("clusters", []):
        for member in cluster.get("members", []):
            rows.append(
                [
                    member.get("hostname"),
                    member.get("deviceIp"),
                    member.get("model"),
                    member.get("serialNumber"),
                    member.get("swVersion"),
                ]
            )

    return rows


def main():
    try:
        rows = get_inventory()
    except requests.exceptions.Timeout:
        raise RuntimeError(
            "The request to GigaVUE-FM timed out after 30 seconds"
        )
    except requests.exceptions.HTTPError as error:
        raise RuntimeError(
            f"GigaVUE-FM returned an HTTP error: {error}"
        )
    except requests.exceptions.ConnectionError as error:
        raise RuntimeError(
            f"Could not connect to GigaVUE-FM: {error}"
        )
    except requests.exceptions.JSONDecodeError as error:
        raise RuntimeError(
            "GigaVUE-FM returned an invalid JSON response"
        ) from error

    if not rows:
        print("No managed devices were found.")
        return

    print(
        tabulate(
            rows,
            headers=[
                "Hostname",
                "IP",
                "Model",
                "Serial",
                "Version",
            ],
            tablefmt="grid",
        )
    )


if __name__ == "__main__":
    main()
