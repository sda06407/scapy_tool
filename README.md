# scapy_tool

Usage:
sudo python3 scapy_tool.py -t [ip] -m scan -s [first port] -e [last port]\n
sudo python3 scapy_tool.py -t [ip] -m exploit_ping_flood -n 2048\n
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_syn_flood -n 2048\n
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_all -n 2048\n

add `-d` argument to view in debug mode
