import discord
import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

class Camera():
	async def takePhoto(self):
		try:
			camera=PiCamera()
			camera.capture('/home/pi/ProjetTut/image/maPhoto.jpg')
			camera.stop_preview()
			camera.close()
			return 0
		except:
			return 1