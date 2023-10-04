import datetime
import os
import logging

# Configuration data
required_config = "[Element Master]\nswitch = mute\nvolume = ignore\n"
conf_file_path = "/usr/share/alsa-card-profile/mixer/paths/analog-output.conf.common"
log_file_path = "/var/log/fix_volume.log"

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Function to log messages
def log_message(message):
    logging.info(message)

# Read the content of the .conf file
with open(conf_file_path, 'r') as file:
    conf_content = file.readlines()

# Check if the required configuration is present in the file content
if required_config in ''.join(conf_content):
    result = "Required configuration is already present. Script stopped."
else:
    # Insert the required configuration at line 136
    conf_content.insert(135, required_config)

    # Write the modified content back to the file
    with open(conf_file_path, 'w') as file:
        file.writelines(conf_content)
    result = "Required configuration inserted at line 136. Restarting the computer in progress"

    # Log the outcome
    log_message(result)

    # Restart the computer (Linux specific)
    os.system("reboot")

print(result)
