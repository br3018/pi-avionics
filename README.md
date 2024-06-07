# pi-avionics
Repository for code to run on the raspberry pi for avionics applications

Process for running code on raspberrypi: 
1. Download git on raspberry pi
2. mkdir repos in home directory
3. cd repos
4. git clone https://github.com/br3018/pi-avionics.git
5. To update repo use git pull

# Usage notes
Taking photos with Raspberry Pi Camera Module 3 use camera software here: https://www.raspberrypi.com/documentation/computers/camera_software.html
Be aware some previous camera packages are depreciated! 

Camera should automatically be enabled for Raspberry Pi 

To transfer files from Raspberry Pi to Windows machine use scp user@raspberrypi:send_path recieve_path