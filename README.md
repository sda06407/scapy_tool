# scapy_tool

```
usage: scapy_tool.py [-h] -t TARGET [-s SOURCE_PORT] [-e END_PORT] [-m {scan,exploit_syn_flood,exploit_ping_flood,exploit_all}] [-p PORT] [-n SENT_TIMES] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET             set IP address to scan/attack
  -s SOURCE_PORT        set port to start scan (in scan mode)
  -e END_PORT           set port to stop scan (in scan mode)
  -m {scan,exploit_syn_flood,exploit_ping_flood,exploit_all}
                        select mode to use (in attack mode)
  -p PORT               set port to attack (in attack mode)
  -n SENT_TIMES         set number of packet to sent (in attack mode)
  -d                    set debug mode
```

Usage:
sudo python3 scapy_tool.py -t [ip] -m scan -s [first port] -e [last port] <br />
sudo python3 scapy_tool.py -t [ip] -m exploit_ping_flood -n 2048 <br />
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_syn_flood -n 2048 <br />
sudo python3 scapy_tool.py -t [ip] -p [port] -m exploit_all -n 2048 <br />

add `-d` argument to view in debug mode
