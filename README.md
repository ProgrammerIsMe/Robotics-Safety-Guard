## Introduction

Home safety is one of the basic and important needs for all people. My project is named Safety Guard, mainly used for home security monitoring. Ideation is to develop a user-friendly, self-monitoring robot that can be operated from remote locations for home safety. Designed robot contains an application on mobile phones and smart home security camera on Raspberry Pi so the user could "walk around" the environment remotely.

## Components
Paspberry Pi 3b+, L293D(H-bridge), raspberry camera v2.1, motor*2, wheel*2, power supply(both for raspberry pi and L293D), cabel*n

## Schematics
Robot:
![image](https://github.com/ProgrammerIsMe/Robotics-Safety-Guard/blob/main/schematics/Components.png)
Curcuit:
![image](https://github.com/ProgrammerIsMe/Robotics-Safety-Guard/blob/main/schematics/Schematics.png)

## Usage
Connect your pc/phone and raspberry with the wifi, open the page http://192.168.70.247:5000/(ip address is dynamic, change it according to raspberry pi ip, and port is always 5000) on your computer/ mobile phone browser.
![image](https://github.com/ProgrammerIsMe/Robotics-Safety-Guard/blob/main/schematics/Safety%20Guard.jpg)

## Required libraries
gpozero, mjpg-streamer, flask, flask-socketio

## Reference
[1] Smart Home Security Cameras Market Analysis Report [EB/OL]. https://www.grandviewresearch.com/industry-analysis/smart-home-security-camera-market. 2021-12-12.
[2] Guidance of Raspberry Pi [EB/OL]. https://www.raspberrypi.org/. 2021-12-12.
[3] Support for Raspberry Pi camera via input_raspicam plugin [EB/OL]. https://github.com/jacksonliam/mjpg-streamer. 2021-12-12.
[4] WebSocket Using Flask and Socket-IO. https://medium.com/swlh/implement-a-websocket-using-flask-and-socket-io-python-76afa5bbeae1. 2021-12-17.

