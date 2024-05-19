import requests
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import argparse


# Define the network address and subnet mask
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="which port on IPs to scan", default="631")
parser.add_argument("-i", "--ip", help="ip address to scan", default="172.19.4.0")
parser.add_argument(
    "-s",
    "--subnet",
    help="subnet mask to specify the IP range",
    default="255.255.252.0",
)
args = parser.parse_args()

# Create an IPv4 network object
network = ipaddress.IPv4Network(f"{args.ip}/{args.subnet}")

printer_ip = []


# Function to check port status and write open IP addresses to a file
def check_port(ip):
    url = f"http://{ip}:{args.port}"
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return ip
    except Exception:
        pass
    return None


# Use ThreadPoolExecutor to execute requests concurrently
with ThreadPoolExecutor(max_workers=2048) as executor:
    results = []
    for result in tqdm(
        executor.map(check_port, network.hosts()), total=network.num_addresses
    ):
        results.append(result)

# Filter out None values from results
printer_ip = [ip for ip in results if ip]

# Print ip one by one
for ip in printer_ip:
    print(ip)

# Write the output into txt file
with open("ip_address.txt", "w") as file:
    for ip in printer_ip:
        file.write(f"{ip}\n")
