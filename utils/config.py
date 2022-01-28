dependencies = ["python3", "flask", "ttyd"]

app_info = {
    'name': 'CodeOnTheFly',
    'version': '0.3.0',
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
    'production' : True,
    'host': '0.0.0.0',
    'port': '5000',
    'debug': True,
}

api_output_configuration = {
    # internal: Will return the internal/local IP address
    # external: Will return the external/public IP address
    # localhost: Will return localhost instead of an IP address
    # Custom: Define the IP address manually
    'IP-Address': 'localhost',
}

ttyd_configuration = {
    # Use -1 to disable
    'UID': '1001',
    'GID': '1001',
    'Single-Use': True,
    # Use 0 for random
    'Port': '0',
}
