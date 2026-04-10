# Python Network Automation Tool

## Overview
This project is a Python-based network automation tool that connects to devices or servers over SSH and executes commands automatically.

It reads device information from a YAML file, loads commands from a text file, connects to each target device, runs the commands, and saves the output into text files.

---

## Features
- Connects to multiple devices automatically
- Runs commands from a predefined command list
- Saves command output into timestamped files
- Logs connection success and failure
- Supports error handling for unreachable devices
- Includes a mock version for demonstration without real devices

---

## Technologies Used
- Python
- Netmiko
- PyYAML
- Logging
- Git

---

## Project Structure
```text
Python Network Automation Tool/
├── main.py
├── mock_main.py
├── devices.yaml.example
├── commands.txt
├── requirements.txt
├── .gitignore
├── README.md
├── outputs/
└── venv/
```

---

## How It Works
1. Load device information from `devices.yaml`
2. Load command list from `commands.txt`
3. Connect to each device using SSH
4. Execute commands one by one
5. Save results in the `outputs/` folder
6. Record activity in the log file

---

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Real device version
```bash
python3 main.py
```

### Mock version
```bash
python3 mock_main.py
```

---

## Example Commands

```text
hostname
ip addr
ip route
uname -a
```

---

## Notes
- `devices.yaml` is ignored by Git because it may contain sensitive information such as IP addresses, usernames, and passwords.
- If no real devices are available, the real version may fail to connect. In that case, the mock version can be used for testing and demonstration.

---

## Future Improvements
- Add support for more device types
- Export results to CSV or JSON
- Add concurrency for faster execution
- Build a simple GUI or web dashboard

---

## Author
Emily Jo