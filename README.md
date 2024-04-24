# lan_printer_scanner
Python tool to scan for LAN printer with one known printer IP address

## Installation
### Clone source code
```
git clone https://github.com/Jade233333/lan_printer_scanner.git
```
### Install requirements
```
pip install requirements.txt
```
## Use
```
python scan_printer.py -i [ip address] -s [subnet mask] - p [port number, default 631]
```
## Methology 
The tool is based on the fact that most printers have a web interface on port 631 so `python request` is used to send HTTP requests on that port. Hence it should work on most occasions when a public network is accessed, especially in schools. However subnetting is usually used to manage large-scale networks, so you probably need to know which subnet are the printers on.
