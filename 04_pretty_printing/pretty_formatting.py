"""
Section 04: Pretty Printing and Output Formatting
Transform messy raw output into professional, readable reports

TODO: Complete the formatting exercises to make output beautiful
"""

def main():
    """
    Your pretty printing practice script  
    """
    
    # TODO 1: Import pprint module
    # You'll need: from pprint import pprint
    import netmiko
    from netmiko import ConnectHandler
    import getpass
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

    # TODO 2: Get some raw command output
    # Connect to your device and get 'show version' output
    # Save the messy raw output to compare later
    
    output = connection.send_command('show version')
    print(repr(output))

    # TODO 3: Create basic formatting functions
    # Make a function that adds headers and separators
    # Make the output look professional with borders
    
    print(f"\n{'='*50}")
    print("Formatted 'show version' output:")
    print('='*50)    

    output_lines = output.splitlines()
    for line in output_lines:
        print(f"| {line:<46} |")
    print('='*50)

    # TODO 4: Practice with structured data
    # Create a dictionary with device information
    # Use pprint() to format it nicely
    
    device_info = {
        'hostname': host,
        'username': username,
        'device_type': device['device_type'],
        'os_version': output_lines[0] if output_lines else "Unknown",
        'uptime': output_lines[1] if len(output_lines) > 1 else "Unknown"
    }
    print(f"\n{'='*50}")
    print("\nDevice Information:")
    print('='*50)
    pprint(device_info)
    print('='*50)

    # TODO 5: Format interface data as a table
    # Take 'show ip interface brief' output
    # Try to make it look like a clean table
    
    output = connection.send_command('show ip interface brief')

    print(f"\n{'='*50}")
    print("\nFormatted 'show ip interface brief' output:")
    print('='*50)
    print(f"|{'Interface':<20} | {'IP-Address':<20} | {'OK?':<5} | {'Method':<10} | {'Status':<20} | {'Protocol':<10} |")
    print('-'*110)
    output_lines = output.splitlines()
    for line in output_lines[1:]:  # Skip the header line
        parts = line.split()
        if len(parts) >= 6:
            interface, ip_address, ok, method, status, protocol = parts[:6]
            print(f"| {interface:<20} | {ip_address:<20} | {ok:<5} | {method:<10} | {status:<20} | {protocol:<10} |")
    print('='*50)

    # TODO 6: Compare before and after
    # Show the raw output next to your formatted version
    # See the difference good formatting makes!
    
    raw_output = connection.send_command('show ip interface brief')
    print(f"\n{'='*50}")
    print("\nRaw 'show ip interface brief' output:")
    print('='*50)
    print(raw_output)

    print(f"\nFormatting practice complete!")

    connection.disconnect()
if __name__ == "__main__":
    main()
