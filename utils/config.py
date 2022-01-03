dependencies = ["python3", "flask", "ttyd"]

app_info = {
    'name': 'CodeOnTheFly',
    'version': '0.2.0',
    'author': 'Pedram M.T. (ItsPedram)',
    'author_email': 'me@itspedram.com',
    'license': 'AGPL-3.0',
    'url': 'https://github.com/Its-pedram/CodeOnTheFly',
    'description': 'Run any code in seconds by calling an API.'
}

help_index = { # Depricated
    # Longer help text
    'Info:': "Run any code in seconds by calling an API.",
    'Usage:': "CodeOnTheFly [Args]",
    # Arguments
    'Arguments:': "",
    '   -h, --help': "Show this help message and exit.",
    '   -v': "Print version and exit.",
    '   --ignore-dependencies': "Ignore checking for dependencies.",
}

flask_configuration = {
    'production' : False,
    'host': '0.0.0.0',
    'port': '5000',
    'debug': True,
}

api_output_configuration = {
    # internal: Will return the internal/local IP address
    # external: Will return the external/public IP address
    # localhost: Will return localhost instead of an IP address
    # Custom: Define the IP address manually
    'IP-Address': 'locahost',
}

ALLOWED_EXTENSIONS = {'py', 'cpp', 'java', 'js', 'ts', 'dart', 'go', 'php', 'c', 'cs'}

compilers = {
    '.py': 'python3',
    '.cpp': 'g++',
    '.java': 'javac',
    '.js': 'node',
    '.ts': 'tsc',
    '.dart': 'dart',
    '.go': 'go',
    '.php': 'php',
    '.c': 'gcc',
    '.cs': 'mcs',
}

ttyd_configuration = {
    # Use -1 to disable
    'UID': '1001',
    'GID': '1001',
    'Single-Use': True,
    # Use 0 for random
    'Port': '0',
}

def generate_command(working_dir, file_name, compiler):
    command = "ttyd"
    if ttyd_configuration['UID'] != '-1':
        command += f" -u {ttyd_configuration['UID']}"
    if ttyd_configuration['GID'] != '-1':
        command += f" -g {ttyd_configuration['GID']}"
    if ttyd_configuration['Single-Use']:
        command += " -o"
    command += f" -p {ttyd_configuration['Port']}" + f" --cwd {working_dir}" + f" {compiler}" + f" {file_name}"
    return command
