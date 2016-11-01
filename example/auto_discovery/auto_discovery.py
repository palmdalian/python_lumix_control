import lumix_control
import ssdp

discover = ssdp.discover('urn:schemas-upnp-org:service:ContentDirectory:1')
IP = ""
if len(discover):
	for response in discover:
		location = response.location
		IP = location.split(':60606')[0].replace('http://', '') # Have only tested this on my camera
if IP != "":
	control = lumix_control.CameraControl(IP)