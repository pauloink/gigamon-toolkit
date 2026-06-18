# Gigamon Toolkit

Automation scripts and utilities for managing and troubleshooting
Gigamon environments.

## Tools

### mapTemplate

Automates the creation of map templates through the GigaVUE-FM API.  
GigaVUE-FM connects to the managed device and creates the configured map templates.

- [Documentation](./mapTemplate/)
- Language: Python
- Purpose: Automate and standardize map template creation on Gigamon devices

### Inventory

Retrieves the inventory of devices managed by GigaVUE-FM through its API, providing a centralized view of the Gigamon environment.

- [Documentation](./inventory/)
- Language: Python
- Purpose: Automate inventory collection for devices managed by GigaVUE-FM

## Requirements

- Python 3.10+
- Access to an authorized Gigamon environment
- Valid GigaVUE-FM credentials

## Installation

```bash
git clone https://github.com/pauloink/gigamon-toolkit.git
cd gigamon-toolkit
```

## Security

Use these tools only in environments where you have explicit authorization.  
Never commit passwords, API tokens or sensitive infrastructure information.
