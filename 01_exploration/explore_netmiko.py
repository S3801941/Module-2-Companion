"""
Section 01: Object Exploration Foundations
Learn to explore Python libraries using built-in tools

TODO: Complete the functions below to master object exploration
"""

# TODO: Import the modules you need
# Hint: You'll need netmiko's ConnectHandler and the inspect module

import netmiko
from netmiko import ConnectHandler
import inspect
from netmiko.base_connection import BaseConnection

def main():
    """
    Your exploration playground
    """
    
    # TODO 1: Basic exploration
    # Use dir(ConnectHandler) to see what methods are available
    # Filter out the private methods (ones starting with '_')
    # Print how many public methods you found
    device ={
        'device_type': 'cisco_ios',
        'host': 'devnetsandboxiosxec8k.cisco.com',
        'username': 's3801941',
        'password': 'yL_5IoMsQh7-66x'
    }

    connection = ConnectHandler(**device) 

    print("#"*50)
    print("All Methods")
    print("#"*50)
    print(dir(ConnectHandler))
    print()

    print("#"*50)
    print("Private Methods")
    print("#"*50)

    print (dir('_'))
    print()


    # TODO 2: Get documentation  
    # Use help() to read about the send_command method
    # What parameters does it take? Which are required?
    print("#"*50)
    print("Getting Help")
    print("#"*50)
    help(BaseConnection.send_command)
    print("Got Help!")
    print()


    # TODO 3: Find specific methods
    # Look for all methods that have 'send' in their name
    # How many different ways can you send things to a device?
    print("#"*50)
    print("Methods with Send")
    print("#"*50)
    method = [m for m in dir(BaseConnection) if 'send' in m]
    print (method)
    print()


    # TODO 4: Method signatures
    # Use inspect.signature() to see the parameters for send_command
    # Do the same for send_config_set - how are they different?

    print("#"*50)
    print("Inspecting Signatures")
    print("#"*50)
    print(inspect.signature(BaseConnection.send_command))
    print()
    print(inspect.signature(BaseConnection.send_config_set))

    
    # TODO 5: Exception discovery
    # Import netmiko.exceptions and explore what's available
    # Which exceptions should you be prepared to handle?
    import netmiko.exceptions
    help(netmiko.exceptions)


    print("Exploration complete! You can now investigate any Python library.")

if __name__ == "__main__":
    main()
