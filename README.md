# lan_printer_scanner
Python tool to scan for LAN printer

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
### Scan for printers on LAN
```
python scan_printer.py -i [ip address] -s [subnet mask] - p [port number, default 631]
```
### Print each printer's own IP address
```
python print_ip.py
```
## Methology 
The tool is based on the fact that most printers have a web interface on port 631 so `python request` is used to send HTTP requests on that port. Hence it should work on most occasions when a public network is accessed, especially in schools. However subnetting is usually used to manage large-scale networks, so you probably need to know which subnet are the printers on.

The second part of the project is designed to help users identify which printer they are using right now. When using the scanner, a very common result is that users have access to a bunch of printers but have no idea the actual loaction of a specific printer. So this function solves the problem by requesting all printers to print their own IPs. As a result , when you reach a printer physically, you are able to access to it specificly.
