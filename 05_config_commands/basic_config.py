"""
Section 05: Configuration Commands
Safely make changes to network devices using automation

TODO: Complete the configuration exercises with proper safety practices
"""

def main():
    """
    Your configuration automation script
    """
    
    # TODO 1: Import modules and establish connection
    # Build on your previous connection skills
    # Connect to your lab device securely
    
    import netmiko
    from netmiko import ConnectHandler
    import getpass
    import datetime
    
    print("#"*50)
    print("Getting Connection Details")
    print("#"*50)
    host = input("Hostname/IP: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }
    
    print("#"*50)
    print(f"Attempting to connect to {host}.")
    print("#"*50)
    
    try:
        connection = ConnectHandler(**device)
        print("Connected!")
        print()
    except ConnectionError:
        print(f"An Error has occured when Attempting to connect to {host}.")
        connection.disconnect()
    except:
        print("An Unknown Exception Happened")
        connection.disconnect()

    # TODO 2: Plan your configuration safely
    # ALWAYS verify current config first
    # Use 'show running-config interface' to see current state
    
    command = 'show running-config interface'
    print(f"\n{'='*50}")
    print(f"Executing: {command}")
    print('='*50)

    output = connection.send_command(command)
    print(output)

    # TODO 3: Build configuration command list
    # Create commands to configure a loopback interface
    # Include: interface, ip address, description
    
    # TODO 4: Apply configuration with send_config_set()
    # Use this method for multiple configuration commands
    # Capture and print the output
    
    # TODO 5: Verify the configuration was applied
    # Use 'show running-config interface' again
    # Compare before and after to confirm changes
    
    # TODO 6: SAFETY PRACTICE - Document what you changed
    # Save configuration output to a file with timestamp
    # Always have a record of what automation changed
    

    connection.disconnect()
    print("Configuration exercise complete - changes documented!")

if __name__ == "__main__":
    main()
