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

flask_configuration = {
    # If set to true, this option will switch
    # flask's debug WSGI server with waitress.
    'production' : False,
    # The ip address that you plan for Flask to 
    # listen on.
    'host': '0.0.0.0',
    # The port that you plan for Flask to 
    # listen on.
    'port': '5000',
    # Toggles Flask's debugging features.
    'debug': True,
}

# Use this section to choose which IP will your API output when a session is requested.
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
    'Port': 0,
}
