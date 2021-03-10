# terrarium

Terrarium is an indoor garden automation application that consists of a data system and a control system. Both run as daemons on a Raspberry Pi
 Zero W. The data system collects data from all of the device's sensors once every five seconds and transmits it to AWS Timestream for storage.
 
 
 ### Data System
 
The data system was configured as follows:
1. Create a file `/etc/systemd/system/data_system.service` with the following contents:
     ```
    [Service]
    WorkingDirectory=/home/pi/terrarium
    ExecStart=python3 /home/pi/terrarium/data_system.py
    Restart=always
    StandardOutput=syslog
    StandardError=syslog
    SyslogIdentifier=terrarium_data
    User=pi
    Group=pi
    Environment=TIMESTREAM_ACCESS_KEY_ID=<access_key_id>
    Environment=TIMESTREAM_SECRET_ACCESS_KEY=<secret_access_key>
    [Install]
    WantedBy=multi-user.target
    ```
2. Change the permissions of the file so that is readable and writable by the owner, readable by the group, and readable to everyone: 
    ```shell script
    sudo chmod 644 /etc/systemd/system/data_system.service
   ```
3. Register the service: 
    ```shell script
    sudo systemctl enable data_system`
   ```
4. Start the service: 
    ```shell script
    sudo systemctl start data_system`
   ```
5. Check the system logs to verify it's working: 
    ```shell script
    cat /var/log/syslog
   ```