import plasma
import time
from plasma import plasma2040

NUM_LEDS = 50

led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT)

run = True

led_strip.start()
while run:
    for j in range(3):
        for i in range(NUM_LEDS):
            if i%2 == 0:
                led_strip.set_rgb(i, 255, 0, 0)
            else:
                led_strip.set_rgb(i, 0, 255, 0)
        time.sleep(1)
        for i in range(NUM_LEDS):
            if i%2 == 1:
                led_strip.set_rgb(i, 255, 0, 0)
            else:
                led_strip.set_rgb(i, 0, 255, 0)
        time.sleep(1)
    for j in range(5):
        for i in range(NUM_LEDS):
            if i%2 == 0:
                led_strip.set_rgb(i, 255, 0, 0)
            else:
                led_strip.set_rgb(i, 0, 255, 0)
        time.sleep(0.1)
        for i in range(NUM_LEDS):
            if i%2 == 1:
                led_strip.set_rgb(i, 255, 0, 0)
            else:
                led_strip.set_rgb(i, 0, 255, 0)
        time.sleep(0.1)
    if button_boot.read():
        for i in range(NUM_LEDS):
            led_strip.set_rgb(i, 0, 0, 0)
        led.set_rgb(0, 0, 0)
                

