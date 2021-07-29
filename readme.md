# ios_config

**ios_config.py – configure a set of commands to multiple devices listed**

_James Sanders ' <ciscoguru72' *at* 'yahoo' *dot* 'com' *dot 'au'_

A python script to configure a set of commands to multiple devices listed in a text file. The script read a set of configuration commands from a text file called 'config.txt' and apply them to one or many devices listed in a text file called 'ip_mgmt.txt'.

I'm a network engineer who enjoys writing Python scripts to make life easy for myself and others. As a Python newbie, I'm always learning to improve my code. Therefore, I'm keen to hear your thoughts on my code and how I should improve. Also, I'm eager to hear new ideas and meet likewise people who write network-related Python scripts.

## Why?

I was asked to apply the same SNMP configuration on 600+ switches, and I wasn't going to do this manually :). So I wrote this script to do the task for me.

## Userguide

**./ios_config.py**

or 

**python3 ios_config.py**

The script will apply a set of commands (config.txt) to device(s) listed in a text file (ip_mgmt.txt). You must configure both config.txt and ip_mgmt.txt as shown; otherwise, Python will abort with errors.

**ip_mgmt.txt file format**

![ip_mgmt](https://github.com/Sandworks/images/blob/4a4cc638fc3625473af17f2c5421e458946e1d6e/ip_mgmt.jpg)

This file contains a list of IP addresses you want to apply the configuration to.

**config.txt file format**

![config](https://github.com/Sandworks/images/blob/4a4cc638fc3625473af17f2c5421e458946e1d6e/config.jpg)

This file contains a list of CLI configuration commands that you would enter into a network device manually.
Once you've defined both ip_mgmt.txt and config.txt files, you are ready to run the script (apply the configuration to the devices). We can run the script as shown:

**python3 ios_config.py**

Here is an example output from this script:

![ios_config](https://github.com/Sandworks/images/blob/4a4cc638fc3625473af17f2c5421e458946e1d6e/ios_config.jpg)

The above output only shows the output of one device. This script will repeat the process for the remaining IP addresses listed in the ip_mgmt.txt file.

## Additional Notes:

None.

Enjoy!

James.