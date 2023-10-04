# import datetime

# # This script checks if a specific configuration is present in a .conf.common file. If the configuration
# # is not found, it inserts the configuration at line 136 of the file. Regardless of the outcome,
# # it logs the result and a timestamp to /home/hekel/test/fixVolume.log.

# # Define the required configuration as a string
# required_config = "[Element Master]\nswitch = mute\nvolume = ignore\n"

# # Specify the path to the .conf file
# conf_file_path = "/home/hekel/test/analog-output.conf.common"

# # Read the content of the .conf file
# with open(conf_file_path, 'r') as file:
#     conf_content = file.readlines()

# # Check if the required configuration is present in the file content
# if required_config in ''.join(conf_content):
#     result = "Required configuration is already present. Script stopped."
# else:
#     # Insert the required configuration at line 136
#     conf_content.insert(135, required_config)

#     # Write the modified content back to the file
#     with open(conf_file_path, 'w') as file:
#         file.writelines(conf_content)
#     result = "Required configuration inserted at line 136."

# # Create a timestamp
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# # Log the outcome to the specified log file
# log_file_path = "/home/hekel/test/fixVolume.log"
# with open(log_file_path, 'a') as log_file:
#     log_file.write(f"{timestamp}: {result}\n")

# print(result)


# import datetime
# import os
# import subprocess

# # This script checks if a specific configuration is present in a .conf file. If the configuration
# # is not found, it inserts the configuration at line 136 of the file. If it inserts the
# # configuration, it will restart the computer and log the result and a timestamp to
# # /home/hekel/test/fixVolume.log.

# # Define the required configuration as a string
# required_config = "[Element Master]\nswitch = mute\nvolume = ignore\n"

# # Specify the path to the .conf file
# conf_file_path = "/home/hekel/test/analog-output.conf.common"

# # Read the content of the .conf file
# with open(conf_file_path, 'r') as file:
#     conf_content = file.readlines()

# # Check if the required configuration is present in the file content
# if required_config in ''.join(conf_content):
#     result = "Required configuration is already present. Script stopped."
# else:
#     # Insert the required configuration at line 136
#     conf_content.insert(135, required_config)

#     # Write the modified content back to the file
#     with open(conf_file_path, 'w') as file:
#         file.writelines(conf_content)
#     result = "Required configuration inserted at line 136. Restarting the computer..."

#     # Create a timestamp
#     timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     # Log the outcome to the specified log file
#     log_file_path = "/home/hekel/test/fixVolume.log"
#     with open(log_file_path, 'a') as log_file:
#         log_file.write(f"{timestamp}: {result}\n")

#     # Restart the computer (Linux specific)
#     os.system("reboot")

# print(result)


import datetime
import os
import logging

# Configuration data
required_config = "[Element Master]\nswitch = mute\nvolume = ignore\n"
conf_file_path = "/home/hekel/test/analog-output.conf.common"
log_file_path = "/home/hekel/test/fixVolume.log"

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
