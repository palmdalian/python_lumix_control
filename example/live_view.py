import lumix_control
import threading
import subprocess

#This gets more and more out of sync.

IP = "10.0.1.105" #IP of camera
control = lumix_control.CameraControl(IP)
UDP_PORT = 5111

def reload_stream():
	control.start_stream(UDP_PORT)
	threading.Timer(10, reload_stream).start() # The stream times out after about 10 seconds.
	
reload_stream()
args = ['ffplay', '-v', 'quiet', 'udp://@:' + str(UDP_PORT)] #FFPlay handles all of the hard decoding stuff automatically
subprocess.check_call(args)
