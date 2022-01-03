import os
import uuid
import tempfile
import socket
import ipaddress
import config
import re
from requests import get
from shutil import which

def is_root():
    return os.geteuid() == 0

def check_dependencies():
    need_dependencies = False
    """
    Checks if the dependencies are installed.
    """
    for dependency in config.dependencies:
        if not which(dependency):
            print("[❌] Please install the following dependency: " + dependency + "\n")
            exit(1)

def show_help(): # Depricated
    for key, value in config.help_index.items():
        print(key, (15-len(key))*" ", value)


def create_workspace():
    """
    Creates the workspace directory.
    """
    folder_name = str(uuid.uuid4())
    temp_folder = tempfile.gettempdir()
    workspace_path = os.path.join(temp_folder, folder_name)
    if not os.path.exists(workspace_path):
        os.makedirs(workspace_path)
    return workspace_path

def is_allowed(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

def which_compiler(file_name):
    extention = file_name.rsplit('.', 1)[1].lower()
    return config.compilers[extention]

def get_ip():
    if config.api_output_configuration['IP-Address'] == "External":
        return get('https://api.ipify.org').text
    elif config.api_output_configuration['IP-Address'] == "Internal":
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    return config.api_output_configuration['IP-Address']

def validate_config():
    # Check if the IP address is valid (Is going to change to a more robust method later)
    if config.api_output_configuration['IP-Address'] not in ["external", "internal", "localhost"]:
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", config.api_output_configuration['IP-Address']):
            print("[❌] Invalid IP adresss detected, please check the IP-Address configuration.")
            exit(1)