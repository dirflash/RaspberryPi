import RPi.GPIO as GPIO

LedPin = 11
TiltPin = 12

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, GPIO.HIGH)

def loop():
    while True:
        if GPIO.input(TiltPin) == GPIO.LOW:
            GPIO.output(LedPin, GPIO.LOW)
            print 'LED ON...'

        else:
            GPIO.output(LedPin, GPIO.HIGH)
            print '          ...LED OFF'

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

