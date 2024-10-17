import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# Setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39,
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

def map_volume_to_leds(volume, num_leds):
    max_volume = 40000
    led_threshold = max_volume // num_leds
    return min(volume // led_threshold, num_leds)

while True:
    volume = microphone.value

    num_leds_on = map_volume_to_leds(volume-18000, len(leds))

    for i in range(len(leds)):
        if i < num_leds_on:
            leds[i].value = True
        else:
            leds[i].value = False

    print(f"Volume: {volume}, LEDs on: {num_leds_on}")

    sleep(0.2)
