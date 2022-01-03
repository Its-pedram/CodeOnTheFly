#! /usr/bin/python3

import os
import sys
import argparse
import utils.ttyd as ttyd
import utils.utils as utils # Don't you love to see this?
import utils.config as config
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.wrappers import response

utils.validate_config()

CodeOnTheFly = Flask(__name__)

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


@CodeOnTheFly.errorhandler(404) 
def invalid_route(e): 
    return f"""
    The requested page was not found!<br>CodeOnTheFly {config.app_info["version"]}
    """, 404

@CodeOnTheFly.route('/', methods=['POST'])
def handle_api():
   if request.method == 'POST':
      if 'code' not in request.files:
            print("No file uploaded!")
      file = request.files['code']
      if file and utils.is_allowed(file.filename):
            filename = secure_filename(file.filename)
   return ttyd.generate_session(
      utils.create_workspace(), filename,
      utils.get_compiler(filename))

if __name__ == '__main__':
   if config.flask_configuration['production']:
      print("[ℹ️] Running in production mode.")
      # from waitress import serve
      # serve(CodeOnTheFly,
      # host=config.flask_configuration['host'],
      # port=config.flask_configuration['port'],)
   else:
      print("[ℹ️] Running in non-production mode.")
      CodeOnTheFly.run(host=config.flask_configuration['host'],
      port=config.flask_configuration['port'],
      debug=config.flask_configuration['debug'])