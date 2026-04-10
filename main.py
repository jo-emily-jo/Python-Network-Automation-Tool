from netmiko import ConnectHandler
import yaml
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(
    filename="automation.log",
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
    output_file = OUTPUT_DIR / f"{host}_{timestamp}.txt"
    with open(output_file, "w") as f:
        f.write(content)

def run_commands_on_device(device, commands):
    host = device["host"]
    try:
        logging.info(f"Connecting to {host}")
        connection = ConnectHandler(**device)

        combined_output = []
        for command in commands:
            logging.info(f"Running '{command}' on {host}")
            output = connection.send_command(command)
            combined_output.append(f"$ {command}\n{output}\n")

        save_output(host, "\n".join(combined_output))
        connection.disconnect()
        logging.info(f"Completed {host}")

    except Exception as e:
        logging.error(f"Failed on {host}: {e}")
        print(f"Error connecting to {host}: {e}")

def main():
    devices = load_devices("devices.yaml")
    commands = load_commands("commands.txt")

    for device in devices:
        run_commands_on_device(device, commands)

if __name__ == "__main__":
    main()