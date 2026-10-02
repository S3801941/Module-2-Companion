"""
Section 06: Parsing with NTC-Templates  
Convert raw text output into structured data for easy processing

TODO: Complete the parsing exercises to see structured data magic
"""

def main():
    """
    Your parsing practice script
    """
    
    # TODO 1: Import required modules
    # You'll need your connection modules from previous exercises
    # You'll also need: from ntc_templates.parse import parse_output
    
    import netmiko
    from netmiko import ConnectHandler
    import getpass
    import datetime
    from pprint import pprint
    from ntc_templates.parse import parse_output

    # TODO 2: Connect and get raw output
    # Connect to your device securely
    # Get 'show version' output and save it as raw text
    
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

    command = 'show version'
    print(f"\n{'='*50}")
    print(f"Executing: {command}")
    print('='*50)

    output = connection.send_command(command)
    print(repr(output))
    print(f"{'='*50}\n")

    # TODO 3: Compare raw vs parsed
    # Print the first 200 characters of raw output (ugly!)
    # Then use parse_output() to convert it to structured data
    
    print(f"\n{'='*50}")
    print("Raw Output")
    print('='*50)
    raw_snippet = output[:200]
    print(f"Raw Output Snippet (first 200 chars):\n{raw_snippet}")
    print(f"{'='*50}\n")

    # I am Parsing the output now
    # TODO 4: Access parsed data easily
    # Extract hostname, version, and uptime from the parsed data
    # Compare how easy this is vs string manipulation!

    print(f"\n{'='*50}")
    print("Completely Parsed Output")
    print('='*50)
    parsed_data = parse_output(platform='cisco_ios', command=command, data=output)
    pprint(parsed_data)
    print(f"{'='*50}\n")

    print(f"\n{'='*50}")
    print("Specific Parsed Data")
    print('='*50)
    if parsed_data:
        device_info = parsed_data[0]  # Assuming the first item contains the device info
        hostname = device_info.get('hostname', 'N/A')
        version = device_info.get('version', 'N/A')
        uptime = device_info.get('uptime', 'N/A')
        print(f"Hostname: {hostname}")
        print(f"Version: {version}")
        print(f"Uptime: {uptime}")
    else:
        print("Parsed data is empty or not in expected format.")
    print(f"{'='*50}\n")
    
    # TODO 5: Parse interface data
    # Get 'show ip interface brief' output
    # Parse it and loop through the interfaces
    # Print interface name and status for each
    
    interface_command = 'show ip interface brief'
    print(f"\n{'='*50}")
    print(f"Executing: {interface_command}")
    print('='*50)
    interface_output = connection.send_command(interface_command)
    parsed_interfaces = parse_output(platform='cisco_ios', command=interface_command, data=interface_output)
    print(f"\n{'='*50}")
    print("Parsed Interface Data")
    print('='*50)
    pprint(parsed_interfaces)
    print(f"{'='*50}\n")
    
    print(f"\n{'='*50}")
    print("Structured Parsed Interface Data")
    print('='*50)
    if parsed_interfaces:
        for interface in parsed_interfaces:
            name = interface.get('interface', 'N/A')
            ip_address = interface.get('ip_address', 'N/A')
            protocol = interface.get('proto', 'N/A')
            status = interface.get('status', 'N/A')
            print(f"Interface: {name}, IP Address: {ip_address}, Protocol: {protocol} Status: {status}")
    else:
        print("Parsed interface data is empty or not in expected format.")

    # TODO 6: Experiment with other commands
    # Try parsing 'show ip route' or other commands
    # See what structured data is available
    
    ip_route_command = 'show ip route'
    print(f"\n{'='*50}")
    print(f"Executing: {ip_route_command}")
    print('='*50)
    ip_route_output = connection.send_command(ip_route_command)
    parsed_routes = parse_output(platform='cisco_ios', command=ip_route_command, data=ip_route_output)
    print(f"\n{'='*50}")
    print("Parsed IP Route Data")
    print('='*50)    
    pprint(parsed_routes)
    print(f"\n{'='*50}")
    print("Structured Parsed IP Route Data")
    print('='*50)
    if parsed_routes:
        for route in parsed_routes:
            network = route.get('network', 'N/A')
            prefix = route.get('prefix_length', 'N/A')
            protocol = route.get('protocol', 'N/A')
            next_hop = route.get('nexthop_if', 'N/A')
            print(f"Route: {network}/{prefix}, Protocol: {protocol}, Next Hop: {next_hop}")
        print(f"{'='*50}\n")
    else:
        print("Parsed route data is empty or not in expected format.")



    connection.disconnect()
    print("Parsing practice complete - structured data is powerful!")

if __name__ == "__main__":
    main()
