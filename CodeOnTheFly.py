#! /usr/bin/python3

import sys
import argparse
import utils.config as config
import utils.utils as utils # Don't you love to see this?

# Beautiful isn't it?
parser = argparse.ArgumentParser(description='CodeOnTheFly Help Menu')

parser.add_argument('-v', "--version", action='store_true',
                    help='Show the current app version and exit.')
parser.add_argument("--no-check", action='store_true',
                    help='Ignore checking for dependencies.')

# Parse them all!
args = parser.parse_args()

if args.version: print(config.app_info['version']), exit(0)

print(f"""
   ______          __     ____      ________         ________     
  / ____/___  ____/ /__  / __ \____/_  __/ /_  ___  / ____/ /_  __
 / /   / __ \/ __  / _ \/ / / / __ \/ / / __ \/ _ \/ /_  / / / / /
/ /___/ /_/ / /_/ /  __/ /_/ / / / / / / / / /  __/ __/ / / /_/ / 
\____/\____/\__,_/\___/\____/_/ /_/_/ /_/ /_/\___/_/   /_/\__, /  
                                                         /____/   
By {config.app_info["author"]} - Version: {config.app_info["version"]}
""")

if not args.no_check: utils.check_dependencies()

