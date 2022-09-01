#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# L298N pins to Raspberry Pi GPIO

right_motor_en = 4
right_motor_a = 14
right_motor_b = 15

left_motor_a = 24
left_motor_b = 23
left_motor_en = 25



GPIO.setmode(GPIO.BCM)

GPIO.setup(right_motor_en , GPIO.OUT)
GPIO.setup(right_motor_a  , GPIO.OUT)
GPIO.setup(right_motor_b , GPIO.OUT)

GPIO.setup(left_motor_a , GPIO.OUT)
GPIO.setup(left_motor_b , GPIO.OUT)
GPIO.setup(left_motor_en , GPIO.OUT)


pwm_r = GPIO.PWM(right_motor_en, 1000)
pwm_l = GPIO.PWM(left_motor_en, 1000)

pwm_r.start(75)
pwm_l.start(75)

def forward(second):
    #print("moving forward")
    GPIO.OUTPUT(right_motor_a, GPIO.HIGH)
    GPIO.OUTPUT(right_motor_b, GPIO.LOW)

    GPIO.OUTPUT(left_motor_a, GPIO.LOW)
    GPIO.OUTPUT(left_motor_b, GPIO.HIGH)

def reverse():
    #print("moving reverse")
    GPIO.OUTPUT(right_motor_a, GPIO.LOW)
    GPIO.OUTPUT(right_motor_b, GPIO.HIGH)

    GPIO.OUTPUT(left_motor_a, GPIO.HIGH)
    GPIO.OUTPUT(left_motor_b, GPIO.LOW)

def left():
    #print("moving left")
    GPIO.OUTPUT(right_motor_a, GPIO.HIGH)
    GPIO.OUTPUT(right_motor_b, GPIO.LOW)

    GPIO.OUTPUT(left_motor_a, GPIO.LOW)
    GPIO.OUTPUT(left_motor_b, GPIO.LOW)

def right():
    #print("moving forward")
    GPIO.OUTPUT(right_motor_a, GPIO.LOW)
    GPIO.OUTPUT(right_motor_b, GPIO.LOW)

    GPIO.OUTPUT(left_motor_a, GPIO.LOW)
    GPIO.OUTPUT(left_motor_b, GPIO.HIGH)

def stop():
    #print("moving stop")
    GPIO.OUTPUT(right_motor_a, GPIO.LOW)
    GPIO.OUTPUT(right_motor_b, GPIO.LOW)

    GPIO.OUTPUT(left_motor_a, GPIO.LOW)
    GPIO.OUTPUT(left_motor_b, GPIO.LOW)


def exit_():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(2)
    right(2)
    stop(2)
    exit_(2)


if __name__=='__main__':
    main()