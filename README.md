# esp32cam
Esp32 cam that can be accessed everywhere by multiple people at once

Clone this repo.

Download esp32cam library to Arduino IDE.

Download here: https://github.com/yoursunny/esp32cam

Change the SSID and Password and upload esp32webserver.ino to your AI thinker Esp32-cam.

Download the server_side folder to your server. I recommend Google cloud VMs running ubuntu
You need to allow ports 8000 and 5000 on your server and port forwarding.

How to allow port forwarding:
  sudo nano /etc/ssh/sshd_config
  in the file:
    UsePAM yes
    AllowTcpForwarding yes
    GatewayPorts yes
    X11Forwarding yes
    PrintMotd no
    PermitTunnel yes

On your server(Ubuntu):
  sudo apt-get update
  sudo apt install python3
  sudo apt install python3-pip
  pip install flask
  pip install opencv-python 
  sudo apt-get install libgl1-mesa-glx
  python3 program.py

On your computer(Windows):
  Lauch connect.bat
  Write your username to access the server with ssh
  Write the ip address of the server
  Write the ip address of the esp32 camera
  It will automaticly login in the server and host an site on http://x:5000 (change x with ip address of your server)



