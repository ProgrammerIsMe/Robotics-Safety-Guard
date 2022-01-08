from flask import Flask, request, jsonify
from flask_socketio import SocketIO, join_room, emit, send
import signal
import sys
import RPi.GPIO as GPIO          
from time import sleep

# GPIO pins
in1 = 23
in2 = 24
in3 = 18
in4 = 25

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

print("Control the robot remotely")


app = Flask(__name__, static_url_path="")
#app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@socketio.on("set_axis")
def set_axis(data):
    print("remote control", data["x"],data["y"]) # data sent back
    motor_control(data["x"],data["y"])

@socketio.on("connect")
def connect():
    print("Connected successfully..")
    
@socketio.on("message")
def socket(message):
    print("received message:",message['data'])

def auto_control():
    robot_forward()
    sleep(2);
    robot_backward()
    sleep(2);
    robot_right()
    sleep(2)
    robot_left()
    sleep(2)
    robot_stop()

def motor_control(x, y):
    if x == 0 and y == 0:
        robot_stop()
    elif (x > -0.2 and x < 0.2) and y > 0:
        robot_backward()
    elif (x > -0.2 and x < 0.2) and y < 0:
        robot_forward()
    elif (y > -0.2 and y < 0.2) and x < 0:
        robot_left()
    elif (y > -0.2 and y < 0.2) and x > 0:
        robot_right()
    else:
        print('other situations')
        

def robot_forward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print("f")
    return

def robot_backward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("b")
    return
    
def robot_left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("l")
    return
    
def robot_right():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print("r")
    return

def robot_stop():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    print("s")
    
    
if __name__ == "__main__":
    #auto_control()
    socketio.run(app, debug=False, host="0.0.0.0")
