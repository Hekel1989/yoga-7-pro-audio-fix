# Yoga 7 Pro-Slim/Realtek® ALC3306 Audio Fix

In laptops with the Realtek ALC3306 audio card,there's an issue with current and past kernels when using Alsa Mixer; the Master volume gets triggered by the volume keys of the laptops, but the PCM volume gets immediately set to 100%, no matter the Master volume level. This directly set the volume of the speakers to 100%.

When Alsa Mixer gets updated, the original file gets restored, thus removing the fix.

This scripts aims to automate this process by checking for the presence of the strings required at boot, and, if missing, re populating the file, and issuing a reboot.
This is achieved through a Python script that is run by a systemd service.

Follow the instructions below to configure it on your machine:

1. **Create a systemd Service File:**

   Create a new systemd service file for your script. Place this file in the `/etc/systemd/system/` directory with a `.service` extension, such as `/etc/systemd/system/fix_volume.service`. Use the template below as reference:

   ```plaintext
   [Unit]
   Description=Launch a script to fix the binary volume issue with this laptop.

   [Service]
   ExecStart=/usr/bin/python3 /path/to/your/script.py
   User=root
   Group=root
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
   ```

   - Replace `/path/to/your/script.py` with the actual path to your Python script.

2. **Reload systemd:**

   After creating the service file, you need to reload the systemd manager to pick up the new service:

   ```bash
   sudo systemctl daemon-reload
   ```

3. **Enable and Start the Service:**

   To enable the service to start at boot, use the following commands:

   ```bash
   sudo systemctl enable fix_volume.service
   ```

4. **Start the Service:**

   You can start the service immediately with:

   ```bash
   sudo systemctl start fix_volume.service
   ```

   This will execute your script as root.

5. **Check the Service Status:**

   You can check the status of the service to ensure it's running and see any potential errors:

   ```bash
   sudo systemctl status fix_volume.service
   ```
   