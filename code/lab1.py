    

x = input("Enter the server name: ")
server_list = ["server1", "server2", "server3"]
servers = {"server1": "on", "server2": "off", "server3": "on"}
try:
    if x not in servers:
        raise ValueError("Server does not exist")   
except TypeError as ve:
    print(f"Error: {ve}")
print(f"{x} is {servers[x]}")
