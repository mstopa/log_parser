import datetime
import random
from pathlib import Path

# Define lists of values for generating logs
event_numbers = [str(i).zfill(3) for i in range(1, 1000)]
ip_addresses = [
    "192.168.1.100",
    "10.0.0.5",
    "172.16.0.20",
    "192.168.2.75",
    "10.1.1.10",
    "192.168.3.200",
    "172.16.1.30",
    "192.168.4.55",
    "10.2.2.5",
    "192.168.5.10",
    "172.16.2.40",
    "10.0.0.15",
    "192.168.6.25",
    "10.1.2.20",
    "172.16.3.50",
    "192.168.7.30",
    "10.2.3.5",
    "192.168.8.15",
    "172.16.4.60",
]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
event_names = [
    [
        f"{letter}000000010",
        f"{letter}00000010",
        f"{letter}0000010",
        f"{letter}000010",
        f"{letter}00010",
        f"{letter}0010",
        f"{letter}010",
        f"{letter}10",
        f"{letter}0",
    ]
    for letter in letters
]
event_names = [item for sublist in event_names for item in sublist]

intervals = [f"every{number}" for number in range(1, 20)]
paths = [
    "/network/routing/ipv4",
    "/system/security/firewall/rules",
    "/etc/loadbalancer/traffic",
    "/network/security/access",
    "/system/vpn/connectivity",
    "/network/dns/queries",
    "/etc/routing/ipv6",
    "/system/loadbalancer/rules",
    "/etc/security/threats",
    "|auth|users",
    "/network/routing/ipv4",
    "/system/security/firewall/rules",
    "/etc/loadbalancer/traffic",
    "|auth|access",
    "/network/routing/ipv6",
    "|auth|login",
    "/system/loadbalancer/rules",
    "|auth|logout",
    "/system/firewall/access",
    "/system/vpn/users",
]

log_dir = Path("logs")
log_dir.mkdir(exist_ok=True, parents=True)

for i in range(20):
    fpath = log_dir / f"log_{str(i).zfill(2)}.txt"

    with open(fpath, "w") as f:
        for j in range(2900000):  # total 58000000 in 20 files for ~5GB of logs
            hour = random.randint(0, 23)
            minute = random.randint(0, 59)
            second = random.randint(0, 59)
            timestamp = datetime.datetime(2023, 11, 15, hour, minute, second)
            timestamp = timestamp.strftime("%b %d %Y %H:%M:%S UTC")
            event_num = random.choice(event_numbers)
            ip_address = random.choice(ip_addresses)
            event_name = random.choice(event_names) + str(event_num)
            interval = random.choice(intervals)
            path = random.choice(paths)
            log = f"{timestamp} [{ip_address}] eventnum={event_num} {event_name} {interval} {path}"
            f.write(log + "\n")
