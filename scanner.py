#!/usr/bin/python

import socket
import subprocess
import sys
from datetime import datetime

def scanPort(address):
    subprocess.call('clear', shell=True)
    ip = socket.gethostbyname(address)
    print "*" * 60
    print "Please wait, scanning host: ", ip
    print "*" * 60
    time1 = datetime.now()
    try:
        for port in range(1, 10000):
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.settimeout(0.2)
            result = server.connect_ex((ip, port))
            if result == 0:
                print("\033[92mPort: {} is Open\033[00m" .format(port))
            else:
                print "Port: %d is Closed" % port
            server.close()
    except KeyboardInterrupt:
        print "You pressed Ctrl + C"
        sys.exit()
    except socket.gaierror:
        print "Host could not be resolved."
        sys.exit()
    except socket.error:
        print "Couldn't connect to server."
        sys.exit()
    time2 = datetime.now()
    total = time2 - time1
    print "Scanning completed in: %d" % total

def portStatus(address, port):
    ip = socket.gethostbyname(address)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(0.2)
    result = server.connect_ex((ip, port))
    if result == 0:
        print "Port: %d is Open" % port
    else:
        print "Port: %d is Closed" % port
    server.close()

def main():
    if len(sys.argv) == 3:
        portStatus(str(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) == 2:
        scanPort(str(sys.argv[1]))
    else:
        print "Wrong arguments!"

main()
