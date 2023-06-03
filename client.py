import socket
import json
from app import App

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
    Create a socket object.
"""

host = '127.0.0.1'  
port = 9999  
"""
    Set the server's IP address and port.
    host: IP server address.
    port: Server port.
"""

s.connect((host, port))
"""
    Connection to hostname on the port.
"""

client_app = App()
"""
    Create an instance of the App class.
"""

values = client_app.collect_user_data()
"""
    Collect user data
"""

list_data = client_app.validate_data(values)
final_data = client_app.generate_dict(list_data)
"""
    Process user data
"""

data = json.dumps(final_data)
"""
    Serialize data to JSON
"""

data = data.encode("ascii")
"""
    Convert data to bytes
"""

s.send(data)
"""
    Send data to the server.
"""


response = s.recv(1024).decode()
"""
# Receive response from the server (no more than 1024 bytes)
"""

response = json.loads(response)
"""
    Convert response from JSON to a dictionary
"""

client_app.menu(response)
"""
    Display the menu using the response data
"""

s.close()
"""
    Close the connection
"""