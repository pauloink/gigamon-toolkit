
# GigaVUE-FM Inventory

A Python script that retrieves the inventory of devices managed by GigaVUE-FM through its REST API.

The inventory is displayed as a table containing each device's hostname, management IP address, model, serial number and software version.

## Features

- Connects to the GigaVUE-FM REST API
- Retrieves devices from all managed clusters
- Displays inventory in a readable table
- Shows hostname, IP address, model, serial number and software version
- Loads authentication credentials from an environment variable

## Requirements

- Python 3.10+
- Access to GigaVUE-FM
- Valid GigaVUE-FM API credentials
- Network access to the GigaVUE-FM API

## Installation

From the repository root:

```bash
cd inventory
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

Never commit the `.env` file or real credentials.

## Configuration

Before running the script, edit the GigaVUE-FM API address in `inventory.py`:

```python
BASE_URL = "https://your-gigavue-fm.example.com/api/v1.3"
```

Replace the example address with the URL of your GigaVUE-FM instance.

## Usage

Run the script from the `inventory` directory:

```bash
python inventory.py
```

Example output:

```text
+------------+---------------+---------+------------+----------+
| Hostname   | IP            | Model   | Serial     | Version  |
+============+===============+=========+============+==========+
| device-01  | 192.0.2.10    | Example | XXXXXXXX   | 6.x.x    |
+------------+---------------+---------+------------+----------+
| device-02  | 192.0.2.11    | Example | XXXXXXXX   | 6.x.x    |
+------------+---------------+---------+------------+----------+
```

The values shown above are fictional examples.

## Returned information

The script displays the following fields:

| Field | Description |
|---|---|
| Hostname | Device hostname |
| IP | Device management IP address |
| Model | Gigamon device model |
| Serial | Device serial number |
| Version | Installed software version |

## Security considerations

- Use this script only in environments where you have explicit authorization.
- Never store credentials directly in the source code.
- Never commit the `.env` file.
- Inventory output may contain sensitive infrastructure information.
- Do not publish real hostnames, IP addresses or serial numbers.
- Avoid sharing terminal screenshots containing real inventory data.

## TLS certificate validation

The current script uses `verify=False`, which disables TLS certificate validation.

This may be necessary in a laboratory environment using self-signed certificates, but it is not recommended for production. Whenever possible, use a trusted certificate and enable TLS validation.

## Disclaimer

This project is not affiliated with or endorsed by Gigamon. Use it at your own risk and only in authorized environments.
