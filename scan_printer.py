import requests
import ipaddress
from concurrent.futures import ThreadPoolExecutor

# Define the network address and subnet mask
network_address = "172.19.4.0"
subnet_mask = "255.255.252.0"
port = "631"

# Create an IPv4 network object
network = ipaddress.IPv4Network(f"{network_address}/{subnet_mask}")

# Function to check port status and write open IP addresses to a file
def check_port(ip):
    url = f"http://{ip}:{port}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            print(f"port {port} on {ip} is open")
        else:
            print(f"port {port} on {ip} is closed")
    except requests.RequestException as e:
        print(f"Failed to connect to {ip}:{port} : {e}")

# Use ThreadPoolExecutor to execute requests concurrently
with ThreadPoolExecutor(max_workers=2048) as executor:
    executor.map(check_port, network.hosts())

