import yaml
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    filename="mock_automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_devices(file_path: str):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)["devices"]

def load_commands(file_path: str):
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_output(host: str, content: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = OUTPUT_DIR / f"mock_{host}_{timestamp}.txt"
    with open(output_file, "w") as f:
        f.write(content)

def run_mock_commands_on_device(device, commands):
    host = device["host"]
    logging.info(f"[MOCK] Connecting to {host}")

    fake_outputs = {
        "hostname": host,
        "ip addr": f"inet {host}/24\ninet 127.0.0.1/8",
        "ip route": "default via 192.168.1.1 dev eth0",
        "uname -a": "Linux mock-device 5.15.0 x86_64 GNU/Linux"
    }

    combined_output = []
    for command in commands:
        logging.info(f"[MOCK] Running '{command}' on {host}")
        output = fake_outputs.get(command, f"Mock output for: {command}")
        combined_output.append(f"$ {command}\n{output}\n")

    save_output(host, "\n".join(combined_output))
    logging.info(f"[MOCK] Completed {host}")
    print(f"[MOCK] Success on {host}")

def main():
    devices = load_devices("devices.yaml")
    commands = load_commands("commands.txt")

    for device in devices:
        run_mock_commands_on_device(device, commands)

if __name__ == "__main__":
    main()