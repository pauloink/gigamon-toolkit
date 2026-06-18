
# Gigamon Map Template Creator

A Python script that automates the creation of map templates on Gigamon devices through the GigaVUE-FM API.

The script sends predefined filtering rules to GigaVUE-FM, creates the map template on each configured cluster and saves the resulting configuration.

## Features

- Creates map templates through the GigaVUE-FM API
- Supports multiple clusters
- Creates IPv4 destination and destination-port matches
- Supports individual ports and port ranges
- Saves the configuration after creating each template
- Loads authentication data from an environment variable

## Requirements

- Python 3.10+
- Access to GigaVUE-FM
- Valid API credentials
- Network access to the GigaVUE-FM API

## Installation

From the repository root:

```bash
cd mapTemplate
python -m venv .venv
```

Activate the virtual environment.

### Linux or macOS

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Authentication

Copy the example environment file:

### Linux or macOS

```bash
cp .env.example .env
```

### Windows PowerShell

```powershell
Copy-Item .env.example .env
```

Edit `.env` and provide your Base64-encoded Basic Authentication token:

```env
AUTH_TOKEN=your_basic_auth_token
```

Do not commit the `.env` file or real credentials.

## Configuration

Before running the script, edit these values in `map_template.py`.

### GigaVUE-FM address

```python
BASE_URL = "https://your-gigavue-fm.example.com/api/v1.3"
```

### Template name

```python
TEMPLATE_NAME = "MP-EXAMPLE"
```

### Target clusters

```python
CLUSTER_IDS = [
    "10.33.233.200",
    "10.33.233.201",
]
```

### Map rules

Each rule contains:

1. Destination IPv4 network
2. Subnet mask
3. Destination port or port range
4. Rule description

Example:

```python
rules = [
    (
        "10.20.38.0",
        "255.255.255.0",
        "5060",
        "Example network on destination port 5060",
    ),
    (
        "10.20.46.0",
        "255.255.255.0",
        "1719..1720",
        "Example network on destination ports 1719-1720",
    ),
]
```

Use `..` to represent a port range:

```text
1719..1720
```

## Usage

Run the script from its directory:

```bash
python map_template.py
```

Example output:

```text
=== Processing cluster 10.33.233.200 ===
Creating template MP-EXAMPLE on cluster 10.33.233.200: HTTP 201
Saving configuration on cluster 10.33.233.200: HTTP 200

Completed successfully.
```

## Security considerations

- Use this script only in environments where you have explicit authorization.
- Never store credentials directly in the source code.
- Never commit the `.env` file.
- Review all cluster IDs and rules before execution.
- Test changes in a controlled environment before using them in production.

## TLS certificate validation

The current example uses `verify=False`, which disables TLS certificate validation. This may be useful in a laboratory environment with self-signed certificates, but it is not recommended for production.

Whenever possible, configure a trusted certificate and enable certificate validation.

## Disclaimer

This project is not affiliated with or endorsed by Gigamon. Use it at your own risk and validate all changes before applying them to a production environment.
