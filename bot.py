import threading
import discord
import RPi.GPIO as GPIO
import os
from time import sleep
from discord.ext import commands
from  picamera import PiCamera

class Alarme(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
		buzzer=40
		GPIO.setup(buzzer,GPIO.OUT)
		i=0
		while i<3:
			GPIO.output(buzzer,GPIO.HIGH)
			sleep(1)
			GPIO.output(buzzer,GPIO.LOW)
			sleep(1)
			i=i+1

class Led(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)

		def run(self):
			GPIO.setwarnings(False)
			GPIO.setmode(GPIO.BOARD)
			led=32
			GPIO.setup(led,GPIO.OUT,initial=GPIO.LOW)
			button=16
			GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)
			while GPIO.input(button)==1:
				GPIO.output(led,GPIO.HIGH)
				sleep(1)
				GPIO.output(led, GPIO.LOW)
				sleep(1)

class Camera():
	async def takePhoto(self):
		try:
			camera=PiCamera()
			camera.capture('/home/pi/ProjetTut/maPhoto.jpg')
			camera.stop_preview()
			camera.close()
			return 0
		except:
			return 1

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

class Bot(commands.Bot,discord.Client):
	def __init__ (self):
		super().__init__(command_prefix="!")
		self.add_command(commands.Command(self.fish,name="fish"))
		self.add_command(commands.Command(self.nasapy,name="nasapy"))

	async def on_ready (self):
		print(f"{self.user.display_name} est connecté au serveur.")

	async def fish(self,msg):
		rph=RemotePhotoHandler()
		await msg.channel.send("Voici neuneil !")
		if (await rph.tryToTakePhoto()==0):
			await msg.channel.send(file=discord.File('maPhoto.jpg'))
		else:
			await msg.channel.send(file=discord.File('../Pictures/neuneuil.jpg'))

	async def nasapy(self,msg):
		nasa=Nasa(key="IzmrzVq1oX4o7FMjp1zLMZgDZjjYce8Fxv1BLNZg")
		await msg.channel.send(nasa.picture_of_the_day()["hdurl"])



bot=Bot()
bot.run("ODI0MzAzNDQxNzY5MjY3MjEw.YFtaZw.9xn5lt5O4DApTs7ASzqyGlhXvo4")

