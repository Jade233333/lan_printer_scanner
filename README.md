# lan_printer_scanner
Python tool to scanner for LAN printer with one known printer ip address

## Installation
### Install python3
...

### Install requirements
```
pip install requirements.txt
```

## Use
Edit the IP/address and subnet mask in the `scan_printer.py`
```
python3 scan_printer.py
```
## Methology 
The tool is based on the fact that most printers have a web interface on port 631 so `python request` is used to send http request on that port. Hence it should work on most occasions when a public network is accessed, especially in schools. However subnetting is usually used to manage large-scale network, so you probably need to know which subnet are the printers on.
