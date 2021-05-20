
from Alarme import Alarme
from Camera import Camera
from Led import Led



class RemotePhotoHandler():
	async def tryToTakePhoto(self):
		camera=Camera()
		if (await camera.takePhoto()==0):
			return 0
		else:
			alarme=Alarme()
			led=Led()
			alarme.start()
			led.start()
			return 1