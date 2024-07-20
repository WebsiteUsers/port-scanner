# Made by WebsiteUser/Kristian

import sys
import socket
from datetime import datetime

#Define our target

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) # Translate Hostname to ipv4

else: 
        print("Invalid amount of arguments.")
        print("Syntax: Python3 scanner.py <ip>")

# Add a Banner
print("-" * 50)
print("Port Scanner made by kristian")
print("Scanning Target: "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
        # made for scanning home router
        for port in range(50,85):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                        print(f"Port {port} is open")
                        print("---------------")
                s.close()
                

except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()

except socket.gaierror:
        print("Hostname could not be resolved")
        sys.exit()

except socket.error:
        print("Could not connect to the server.")
        sys.exit()
