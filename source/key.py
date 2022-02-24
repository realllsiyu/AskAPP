
import RPi.GPIO as GPIO

class key():
    #GPIO0 GPIO5 GPIO6 GPIO13
    key_pin = [0,5,6,13]
    key_status=[1,1,1,1]
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        for pin in self.key_pin:
            GPIO.setup(pin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
    def read(self):
        for i in range(4):
            if GPIO.input(self.key_pin[i]):
                self.key_status[i]=1
            else :
                self.key_status[i]=0
        return self.key_status