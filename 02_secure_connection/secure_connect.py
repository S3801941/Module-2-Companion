"""
Section 02: Secure SSH Connection Foundations
Build your first network automation connection using secure practices

TODO: Import the modules you need and complete the connection
"""

def main():
    """
    Your secure connection script
    """
    
    # TODO 1: Import required modules
    # You'll need getpass for secure password input
    # You'll need ConnectHandler from netmiko for the connection
    
    import netmiko
    from netmiko import ConnectHandler
    import getpass


    # TODO 2: Collect connection information from user
    # Use input() for device IP and username
    # Use getpass.getpass() for password (hidden input)
    print("#"*50)
    print("Getting Connection Details")
    print("#"*50)
    host = input("Hostname/IP: ")
    username = input("Username: ")
    password = getpass.getpass("Password: ")


    # TODO 3: Build device dictionary
    # Include device_type: 'cisco_ios'
    # Include the host, username, and password you collected
    
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password
    }

    # TODO 4: Establish connection
    # Use ConnectHandler with your device dictionary
    # Wrap in try/except for error handling
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


    # TODO 5: Test the connection
    # Send a simple command like 'show clock'
    # Print the output to verify it worked
    print("#"*50)
    print("Showing System Clock")
    print("#"*50)
    output = connection.send_command('show clock')
    print(output)
    print()
    print("#"*50)
    print("Showing Run Config")
    print("#"*50)
    output = connection.send_command('show run')
    print(output)

    # TODO 6: Clean up
    # Always disconnect when finished
    
    connection.disconnect()

    print("Connection exercise complete!")

if __name__ == "__main__":
    main()
