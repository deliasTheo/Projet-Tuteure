import threading
import discord
import RPi.GPIO as GPIO
from time import sleep

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