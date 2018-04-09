#!/usr/bin/python3.5
import pigpio
import time
import datetime
import sys
from pygame import mixer

# pigpiod muss auf pi laufen!!!

# TRY CATCH!!!
# Zeit zu welcher der Stripe zu 100% leuchten soll.
if (0):
    alarm_time_year = 2017
    alarm_time_month = 10
    alarm_time_day = 3
    alarm_time_hours = 21
    alarm_time_minutes = 14
    # Fade Time zu end_rgb in Minuten
    fade_time = 10
if (1):
    alarm_time_year = int(sys.argv[1])
    alarm_time_month = int(sys.argv[2])
    alarm_time_day = int(sys.argv[3])
    alarm_time_hours = int(sys.argv[4])
    alarm_time_minutes = int(sys.argv[5])
    # Fade Time zu end_rgb in Minuten
    fade_time = int(sys.argv[6])

pi = pigpio.pi()  # initialise GPIO connection
# set pins
pin_green = 22
pin_red = 24
pin_blue = 17

# end colour
end_r = 254
end_g = 110
end_b = 5

# Zeit in Minuten welche der Stripe in end_rgb leuchtet.
latest_timeout = 30.0

# set GPIO Pins Modes
pi.set_mode(pin_red, pigpio.OUTPUT)
pi.set_mode(pin_green, pigpio.OUTPUT)
pi.set_mode(pin_blue, pigpio.OUTPUT)

# set fade fade_time for rgb
fade_time_r = end_r / (fade_time * 60)
fade_time_g = end_g / (fade_time * 60)
fade_time_b = end_b / (fade_time * 60)

# calculate start time for fading
start_time = datetime.datetime(2000, 1, 1, 1, 1, 1)
jetzt = datetime.datetime.now()
alarm_time = datetime.datetime(alarm_time_year, alarm_time_month, alarm_time_day, alarm_time_hours, alarm_time_minutes)
TIMEDELTA_DURATION = datetime.timedelta(minutes=fade_time)
start_time = alarm_time - TIMEDELTA_DURATION

# set actual rgb values
actual_r = 0
actual_g = 0
actual_b = 0
pi.set_PWM_dutycycle(pin_green, actual_g)
pi.set_PWM_dutycycle(pin_red, actual_r)
pi.set_PWM_dutycycle(pin_blue, actual_b)

#######################Test for working script
pi.set_PWM_dutycycle(pin_green, 0)
pi.set_PWM_dutycycle(pin_red, 10)
pi.set_PWM_dutycycle(pin_blue, 10)
time.sleep(0.5)
pi.set_PWM_dutycycle(pin_green, 0)
pi.set_PWM_dutycycle(pin_red, 0)
pi.set_PWM_dutycycle(pin_blue, 0)
##################
###########
# boolean variables
time_browsing = True
# button_pressed = False
while time_browsing:
    if (start_time < datetime.datetime.now()):
        while (actual_r < 255):
            if (actual_g < 255):
                pi.set_PWM_dutycycle(pin_green, actual_g)
            if (actual_r < 255):
                pi.set_PWM_dutycycle(pin_red, actual_r)
            if (actual_b < 255):
                pi.set_PWM_dutycycle(pin_blue, actual_b)
            print("Aktulle Werte: " + str(int(actual_r)) + " " + str(int(actual_g)) + " " + str(int(actual_b)))
            time.sleep(1)
            actual_g += fade_time_g
            actual_r += fade_time_r
            actual_b += fade_time_b
        time_browsing = False
        # mixer.init()
        # a=mixer.music.load('/home/pi/Desktop/alarm.mp3')
        # mixer.music.play()
    else:
        time.sleep(10)
        print("Warten auf Weckzeit. Aktuelle Uhrzeit:" + str(datetime.datetime.now()))
# while(mixer.music.get_busy()==False):
# time.sleep(2)
# mixer.music.stop()
pi.set_PWM_dutycycle(pin_green, 200)
pi.set_PWM_dutycycle(pin_red, 200)
pi.set_PWM_dutycycle(pin_blue, 200)
time.sleep(60 * 20)
pi.set_PWM_dutycycle(pin_green, 0)
pi.set_PWM_dutycycle(pin_red, 0)
pi.set_PWM_dutycycle(pin_blue, 0)
pi.stop()  # close GPIO connection
print("Program terminated")



