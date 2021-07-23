#!/usr/bin/env python3

# Filename: ios_config.py
# Author:   James Sanders
# Version:  1.0

# Import dependencies
import os
from netmiko import ConnectHandler
from getpass import getpass

# Obtain device credentials
username = input('Username: ')
password = getpass(prompt='password: ')

BACKUP_DIR = "backups/"

def create_backups_dir():
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)

def save_config_to_file(hostname, config):
    filename =  f"{hostname}.cfg"
    print("Backup Config - ", filename)
    with open(os.path.join(BACKUP_DIR, filename), "w") as f:
        f.write(config)

# Create backup folder if non-exist
create_backups_dir()

# Upload config set from file
# Note: Config line are import to lines as list
with open('rollback.txt') as config:
    lines = config.read().splitlines()

# Open device IP file
ipfile = open('ip_mgmt.txt', 'r') 

# Process - Backup running-config file, rollback config changes and save to NVRAM.
for ipaddress in ipfile:

    device = {
        'device_type': 'cisco_ios',
        'ip': ipaddress,
        'username': username,
        'password': password
    }

    # Connect to device
    net_connect = ConnectHandler(**device)

    # Get hostname
    hostname_result = net_connect.send_command("show run | i hostname")
    result = hostname_result.split()
    hostname = result[1]

    # Get running-config
    config = net_connect.send_command("show run")

    # Backup config
    save_config_to_file(hostname, config)

    # Implement config
    print("configuring - ", hostname)
    output = net_connect.send_config_set(lines)
    print (output)

    # Write config
    verify = net_connect.send_command("write")
    print(verify)

print("Rollback Successful")