import os
import uuid
import tempfile
import socket
import ipaddress
import re
import utils.config as config
from utils.language_support import generate_compiler_command, ALLOWED_EXTENSIONS, compilers
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
            print(f"[❌] {dependency} not found. Please install {dependency}.")
            need_dependencies = True
    if need_dependencies:
        exit(1)

def show_help(): # Depricated
    for key, value in config.help_index.items():
        print(key, (15-len(key))*" ", value)

def create_workspace(file, filename):
    """
    Creates the workspace directory.
    """
    folder_name = str(uuid.uuid4())
    temp_folder = tempfile.gettempdir()
    workspace_path = os.path.join(temp_folder, folder_name)
    os.makedirs(workspace_path, mode = 0o777, exist_ok = True)
    file.save(os.path.join(workspace_path, filename))
    return workspace_path

def is_allowed(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def which_compiler(file_name):
    extention = file_name.rsplit('.', 1)[1].lower()
    return compilers["." + extention]

def generate_command(working_dir, file_name, compiler):
    command = "ttyd"
    if config.ttyd_configuration['UID'] != '-1':
        command += f" -u {config.ttyd_configuration['UID']}"
    if config.ttyd_configuration['GID'] != '-1':
        command += f" -g {config.ttyd_configuration['GID']}"
    if config.ttyd_configuration['Single-Use']:
        command += " -o"
    
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()

    command += " -t disableReconnect=true" + f" -p {port}" + f" --cwd {working_dir}" + f" {compiler} " + str(generate_compiler_command(file_name, compiler))
    return command, port

def get_ip(): # Implement a caching method later
    if config.api_output_configuration['IP-Address'] == "external":
        return get('https://api.ipify.org').text
    elif config.api_output_configuration['IP-Address'] == "internal":
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)
    return config.api_output_configuration['IP-Address']

def validate_config():
    # Check if the IP address is valid (Is going to change to a more robust method later)
    if config.api_output_configuration['IP-Address'] not in ["external", "internal", "localhost"]:
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", config.api_output_configuration['IP-Address']):
            print("[❌] Invalid IP adresss detected, please check the IP-Address configuration.")
            exit(1)
    else:
        if config.api_output_configuration['IP-Address'] != "localhost":
            config.api_output_configuration['IP-Address'] = get_ip()
    