"""
Section 03: Show Commands and Raw Output
Execute show commands and see why raw text is challenging

TODO: Build on your secure connection skills to explore command output
"""

def main():
    """
    Your show command exploration script
    """
    
    # TODO 1: Import modules and establish connection
    # Reuse your connection code from Module 02
    # Connect to your lab device securely
    
    import netmiko
    from netmiko import ConnectHandler
    import getpass

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
    
    # TODO 2: Execute basic show commands
    # Try: show clock, show version, show ip interface brief
    # Print the output from each command
    
    commands = ['show clock', 'show version', 'show ip interface brief']

    for command in commands:
        print(f"\n{'='*50}")
        print(f"Executing: {command}")
        print('='*50)

        output = connection.send_command(command)
        print(output)
        print(f"\nRaw length: {len(output)} characters\n")

    # TODO 3: Analyze the raw output structure  
    # Count how many lines each command produces
    # Look at the first and last few lines
    # Use repr() to see the \n and \r characters
    
        print(f"Line count: {len(output.splitlines())} lines\n") # Splitlines needed instead of split.
        first_line = output.splitlines()[0]
        print(f"First line: {first_line}\n") # Outputing the first line
        last_line = output.splitlines()[-1]
        print(f"Last line: {last_line}\n") # Outputting the last line
        print(repr(output))
        print()
        
    # TODO 4: Try to extract specific information
    # From 'show version' - find the hostname
    # From 'show ip interface brief' - find interfaces that are 'up'
    # See how difficult this is with raw text!

    # TODO 5: Save raw output to text files
    # Save each command output to a separate file
    # Open the files in a text editor to see the formatting

    print("Raw output analysis complete!")

if __name__ == "__main__":
    main()
