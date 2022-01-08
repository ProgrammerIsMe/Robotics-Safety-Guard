sudo apt update

# Install GPIO Zero
sudo apt install python3-gpiozero -y

# Install pip for python3
sudo apt install python3-pip -y

# Install mjpg-streamer to stream UVC camera
wget https://github.com/jacksonliam/mjpg-streamer/archive/master.zip
unzip master.zip
rm master.zip
cd mjpg-streamer-master/mjpg-streamer-experimental
sudo apt-get install cmake libjpeg8-dev -y
sudo apt-get install gcc g++ -y
make
sudo make install

# install packages for socket connection
sudo apt install flask
sudo apt install flask-socketio
