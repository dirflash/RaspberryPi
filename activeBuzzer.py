import RPi.GPIO as GPIO
import time

BeepPin = 12                         # pin12

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)         # Numbers pins by physical location
    GPIO.setup(BeepPin, GPIO.OUT)    # Set pins mode as output
    GPIO.output(BeepPin, GPIO.HIGH)  # Set pin to high(+3.3V) to off the beep

def loop():
    while True:
        GPIO.output(BeepPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(0.1)

def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)  # beep off
    GPIO.cleanup()                   # Release resource

if __name__ == '__main__':           # Program start from here
    print "Press CTRL+C to end the program..."
    setup()
    try:
        loop()
    except KeyboardInterupt:         # When 'CTRL+C' is pressed, the child program destroy() will be execture.
        destroy()

