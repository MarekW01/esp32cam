# esp32cam
Esp32 cam that can be accessed everywhere by multiple people at once

Clone this repo.

Download esp32cam library to Arduino IDE.

Download here: https://github.com/yoursunny/esp32cam

Change the SSID and Password and upload esp32webserver.ino to your AI thinker Esp32-cam.

Download the server_side folder to your server. I recommend Google cloud VMs running ubuntu <br />
You need to allow ports 8000 and 5000 on your server and port forwarding. <br />

How to allow port forwarding: <br />
  sudo nano /etc/ssh/sshd_config <br />
  in the file: <br />
    UsePAM yes <br />
    AllowTcpForwarding yes <br />
    GatewayPorts yes <br />
    X11Forwarding yes <br />
    PrintMotd no <br />
    PermitTunnel yes <br />

On your server(Ubuntu): <br />
  sudo apt-get update <br />
  sudo apt install python3 <br />
  sudo apt install python3-pip <br />
  pip install flask <br />
  pip install opencv-python  <br />
  sudo apt-get install libgl1-mesa-glx <br />
  Open templates/index.html and change the ip address on the bottom from x to your server ip  <br />
  python3 program.py <br />

On your computer(Windows): <br />
  Lauch connect.bat <br />
  Write your username to access the server with ssh <br />
  Write the ip address of the server <br />
  Write the ip address of the esp32 camera <br />
  It will automaticly login in the server and host an site on http://x:5000 (change x with ip address of your server) <br />



