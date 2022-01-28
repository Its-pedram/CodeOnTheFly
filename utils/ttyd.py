import utils.utils as utils
import subprocess
import utils.config as config


def generate_session(working_dir, file_name, compiler):
    print(working_dir, file_name, compiler)
    final_command, port = utils.generate_command(working_dir, file_name, compiler)
    print(final_command)
    proc = subprocess.Popen(final_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return config.api_output_configuration['IP-Address'] + ":" + str(port)