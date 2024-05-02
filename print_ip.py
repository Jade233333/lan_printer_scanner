import subprocess
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

def lpr_print_ip(host):
    """
    Print text using the lpr command to the specified host.
    
    Args:
        host (str): The IP address or hostname of the printer.
        text (str): The text to be printed.
    
    Returns:
        bool: True if the print job was successful, False otherwise.
    """
    command = f'echo "{host}" | lpr -H {host}'

    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Print job sent to {host} successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        return False


with open("ip_address.txt") as f:
    ips = f.readlines()
    print(ips)
    with ThreadPoolExecutor() as executor:
        results = []
        for result in tqdm(executor.map(lpr_print_ip, ips), total = len(ips)):
            results.append(result)

