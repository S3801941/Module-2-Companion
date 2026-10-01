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
    from pprint import pprint
    
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
    
    command = 'show running-config'
    print(f"\n{'='*50}")
    print(f"Executing: {command}")
    print('='*50)

    output = connection.send_command(command)
    print(output)
    print(f"{'='*50}\n")

    # TODO 3: Build configuration command list
    # Create commands to configure a loopback interface
    # Include: interface, ip address, description

    loopback_interface = input("Enter Loopback Interface (e.g., Loopback10): ")
    ip_address = input("Enter IP Address (e.g., 10.10.10.10): ")
    description = input("Enter Description for the Interface: ")
    
    config_commands = [
        f'interface {loopback_interface}',
        f'ip address {ip_address} 255.255.255.255',
        f'description {description}',
        'no shutdown'
    ]

    # TODO 4: Apply configuration with send_config_set()
    # Use this method for multiple configuration commands
    # Capture and print the output
    
    print(f"\n{'='*50}")
    print("Applying Configuration Commands")
    print('='*50)

    output = connection.send_config_set(config_commands)
    print(output)

    # TODO 5: Verify the configuration was applied
    # Use 'show running-config interface' again
    # Compare before and after to confirm changes
    
    verify_command = f'show running-config interface {loopback_interface}'
    print(f"\n{'='*50}")
    print(f"Verifying Configuration with: {verify_command}")
    print('='*50)

    verify_output = connection.send_command(verify_command)
    print(verify_output)

    print(f"{'='*50}")

    # TODO 6: SAFETY PRACTICE - Document what you changed
    # Save configuration output to a file with timestamp
    # Always have a record of what automation changed
    
    show_running_config = connection.send_command('show running-config')

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"config_changes_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Configuration changes made on {host} at {timestamp}\n")
        f.write(f"{'='*50}\n")
        f.write("Configuration Commands Applied:\n")
        for cmd in config_commands:
            f.write(f"{cmd}\n")
        f.write(f"\n{'='*50}\n")
        f.write("Verification Output:\n")
        f.write(verify_output)
        f.write(f"\n{'='*50}\n")
        f.write("Current Running Configuration:\n")
        f.write(show_running_config)
        f.write(f"\n{'='*50}")

    connection.disconnect()
    print("Configuration exercise complete - changes documented!")

if __name__ == "__main__":
    main()
