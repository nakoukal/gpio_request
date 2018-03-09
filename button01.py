import RPi.GPIO as GPIO
import time
import urllib.request
import urllib.parse

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:
    url='http://address/teplota/gpio_process.php?action=get'
    while True:
         button_state = GPIO.input(23)
         if button_state == False:
             GPIO.output(24, True)
             f=urllib.request.urlopen(url)
             print(f.read().decode('utf-8'))
             time.sleep(1)
         else:
             GPIO.output(24, False)
except:
    GPIO.cleanup()
