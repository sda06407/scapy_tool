# scapy_tool

Usage:
sudo python3 scapy_tool.py -t [ip] -m scan -s [first port] -e [last port]
sudo python3 scapy_tool.py -t [ip] -m exploit_ping_flood -n 2048
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_syn_flood -n 2048
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_all -n 2048

add `-d` argument to view in debug mode
