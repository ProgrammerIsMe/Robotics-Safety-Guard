mjpg-streamer
=============
mjpg-streamer is a command line application that transmits JPEG frames from one or more input plugins to multiple output plugins. It can be used to stream JPEG files over an IP-based network from a webcam to various types of viewers.


Usage
=====

When launching mjpg-streamer, you specify one or more input plugins and an output plugin. For example, to stream a V4L compatible webcam via an HTTP server (the most common use case), you can do something like this:

	mjpg_streamer -i input_uvc.so -o output_http.so

and the robot use the command like this:
	mjpg_streamer -i "input_uvc.so -d /dev/video0 -f 10 -y" -o "output_http.so -w ./www"


Reference
=====
[1] Support for Raspberry Pi camera via input_raspicam plugin [EB/OL]. https://github.com/jacksonliam/mjpg-streamer. 2021-12-12.

