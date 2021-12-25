import os
from shutil import which
import utils.config as config

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