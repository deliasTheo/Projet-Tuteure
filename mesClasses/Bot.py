import threading
import discord
import RPi.GPIO as GPIO
import os
import nasapy
import random
import urllib.request
from dotenv import load_dotenv
from RPH import RemotePhotoHandler
from Led import Led
from PIL import Image
from time import sleep
from discord.ext import commands

load_dotenv(dotenv_path="../configCle")

imgNasa="../image/imgNasa.png"
imgPoisson="../image/neuneilEspace.png"
imgSuperposes="../image/imgSuperposes.png"
nasa=nasapy.Nasa(key=os.getenv("CLE"))
picture=nasa.picture_of_the_day()

rph=RemotePhotoHandler()


class Bot(commands.Bot,discord.Client):
	def __init__ (self):
		super().__init__(command_prefix="!")
		self.add_command(commands.Command(self.fish,name="fish"))
		self.add_command(commands.Command(self.nasapy,name="nasapy"))
		self.add_command(commands.Command(self.spacefish,name="spacefish"))

	async def on_ready (self):
		print(f"{self.user.display_name} est connecté au serveur.")

	async def fish(self,msg):
		await msg.channel.send("Voici notre petit neuneil !")
		if (await rph.tryToTakePhoto()==0):
			await msg.channel.send(file=discord.File('../image/maPhoto.jpg'))
		else:
			await msg.channel.send(file=discord.File('../image/neuneil.jpg'))

	async def nasapy(self,msg):
		try:
			await msg.channel.send(picture["hdurl"])
		except:
			await msg.channel.send("La photo ne peux pas être envoyer, désolé ^^")            
	async def spacefish(self,msg):
		await msg.channel.send("Décolage de Neuneil dans l'espace")
		try :
			urllib.request.urlretrieve(picture["url"],imgNasa)
			background = Image.open(imgNasa)
			img=Image.open(imgPoisson)
			diviseurLongueur = random.uniform(1.2, 5)
			diviseurHauteur = random.uniform(1.2, 5)
			longueurImg,hauteurImg=background.size
			longueurImg = int(longueurImg / diviseurLongueur)
			hauteurImg = int(hauteurImg / diviseurHauteur)
			background.paste(img,(longueurImg,hauteurImg),img)
			background.save(imgSuperposes,filename=imgSuperposes)
			file2 = discord.File(imgSuperposes, filename=imgSuperposes)
			await msg.channel.send("Neuneil est atterie dans l'espace :slight_smile:", file=file2)
		except :
			await msg.channel.send("Neuneil n'est pas arrivé à destination :slight_frown:")
        

bot=Bot()
bot.run(os.getenv("TOKEN"))

