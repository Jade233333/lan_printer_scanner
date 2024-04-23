import requests
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

# Define the network address and subnet mask
network_address = "172.19.4.0"
subnet_mask = "255.255.252.0"
port = "631"

# Create an IPv4 network object
network = ipaddress.IPv4Network(f"{network_address}/{subnet_mask}")

printer_ip = []

# Function to check port status and write open IP addresses to a file
def check_port(ip):
    url = f"http://{ip}:{port}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return ip
    except:
        pass
    return None

# Use ThreadPoolExecutor to execute requests concurrently
with ThreadPoolExecutor(max_workers=2048) as executor:
    results = []
    for result in tqdm(executor.map(check_port, network.hosts()), total=network.num_addresses):
        results.append(result)

# Filter out None values from results
printer_ip = [ip for ip in results if ip]

# Print ip one by one
for ip in printer_ip:
    print(ip)
