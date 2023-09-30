import time
import random
from rpi_lcd import LCD
from actuator import *
from sensor import *
from send_data import * 
from time import sleep
import RPi.GPIO as GPIO

# Define the servo motor's GPIO pin
SERVO_PIN = 21

# Set up GPIO mode and servo pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)



# Create a PWM object for the servo
servo_pwm = GPIO.PWM(SERVO_PIN, 50)  # 50 Hz frequency

lcd = LCD()

def cleanup():
    # Membersihkan pin GPIO pada Raspberry Pi
    GPIO.cleanup()

try:
    while True:
        print("Silahkan Tap Kartu Anda")
        lcd.text("Silahkan", 1)
        lcd.text("Tap Kartu Anda", 2)
        status = rfid_read()
        print(status)
        
        if status == "berhasil":
            lcd.clear()
            ledgreenon()
            bip_benar()
            lcd.text("Berhasil", 1)
            
            # Rotate the servo to a certain angle for success
            servo_pwm.start(0)  # Start PWM with 0% duty cycle
            servo_pwm.ChangeDutyCycle(2)  # Rotate to the middle position (90 degrees)
            time.sleep(2)
            servo_pwm.ChangeDutyCycle(6)  # Rotate to the middle position (90 degrees)
            time.sleep(0.5)
            #servo_pwm.stop()  # Stop PWM
            
        else:
            lcd.clear()
            ledredon()
            bip_salah()
            lcd.text("Gagal", 1)
            time.sleep(1)
            
        
        # Turn off LED and buzzer, clear LCD
        buzzeroff()
        ledredoff()
        ledgreenoff()
        lcd.clear()

except KeyboardInterrupt:
    # Memberhentikan program dengan menekan Ctrl + C
    cleanup()
