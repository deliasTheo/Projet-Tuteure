import threading
import discord
import RPi.GPIO as GPIO
from time import sleep


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