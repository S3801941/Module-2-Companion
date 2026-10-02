"""
Section 07: Professional Reports with F-Strings
Create polished, professional reports from your network data

TODO: Complete the reporting exercises to build impressive documentation
"""

def main():
    """
    Your professional reporting script
    """
    
    # TODO 1: Import required modules  
    # You'll need datetime for timestamps
    # Build on your parsing skills from Module 06
    
    import netmiko
    from netmiko import ConnectHandler
    import getpass
    import datetime
    from pprint import pprint
    from ntc_templates.parse import parse_output

    # TODO 2: Gather and parse device data
    # Connect to your device and get parsed data
    # Extract hostname, version, uptime, interfaces

    # TODO 3: Create a professional device report
    # Use f-strings to format device information nicely
    # Add headers, separators, and proper alignment
    # Make it look like something you'd show a manager!
    
    # TODO 5: Save timestamped reports
    # Create filenames with dates and times
    # Save your reports to files for documentation
            
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

    print(f"\n{'='*50}")
    print("Gathering Device Data")
    print('='*50)
    commands = ['show version', 'show ip interface brief']
    for command in commands:
        print(f"\n{'='*50}")
        print(f"Executing: {command}")
        print('='*50)
        output = connection.send_command(command)
        print(repr(output))
        if command == 'show version':
            parsed_version = parse_output(platform='cisco_ios', command=command, data=output)
            print(f"\n{'='*50}")
            print("Parsed Version Data")
            print('='*50)
            pprint(parsed_version)

            print(f"\n{'='*50}")
            print("Device Version Report")
            print('='*50)
            # Add a backslash at the end of the first line of the f-string to avoid unwanted newlines
            report = f"""\
report timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Device Report for {parsed_version[0].get('hostname', 'N/A')}
{'-'*70}
Model: {parsed_version[0].get('hardware', 'N/A')}
Serial: {parsed_version[0].get('serial', 'N/A')}
Software Image: {parsed_version[0].get('software_image', 'N/A')}
Version: {parsed_version[0].get('version', 'N/A')}
Uptime: {parsed_version[0].get('uptime', 'N/A')}"""
            print(report)

            with open(f"Command Output Files/device_report_{host}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 'w') as f:
                f.write(report)

        elif command == 'show ip interface brief':
            parsed_interfaces = parse_output(platform='cisco_ios', command=command, data=output)
            print(f"\n{'='*50}")
            print("Parsed Interface Data")
            print('='*50)
            pprint(parsed_interfaces)

            print(f"\n{'='*50}")
            print("Device Interface Report")
            print('='*50)
            # Add a backslash at the end of the first line of the f-string to avoid unwanted newlines
            report = f"""\
report timestamp: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Interface Report for {host}
{'-'*70}
{'Interface':<20}{'IP Address':<20}{'Status':<15}{'Protocol':<15}
{'-'*70}"""
            for interface in parsed_interfaces:
                name = interface.get('interface', 'N/A')
                ip_address = interface.get('ip_address', 'N/A')
                status = interface.get('status', 'N/A')
                protocol = interface.get('proto', 'N/A')
                report += f"""
{name:<20}{ip_address:<20}{status:<15}{protocol:<15}"""
            print(report)

            with open(f"Command Output Files/interface_report_{host}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 'w') as f:
                f.write(report)


    # TODO 4: Add number formatting
    # Format percentages, decimals, and padding properly
    # Practice different f-string formatting options

    # TODO 6: Build a summary report
    # If you have multiple devices, create a summary
    # Show overall network health and status
    
    connection.disconnect()
    print("Professional reporting complete - documentation ready!")

if __name__ == "__main__":
    main()
