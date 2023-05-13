from time import sleep
from random import randrange

fire = False

def fake_temperature():
    global fire
    if(not fire and randrange(1, 10) < 2):
        fire = True

    offset = 0 if not fire else 20
    min = 60 + offset
    max = 70 + offset

    return randrange(min, max)

while True:
    print(fake_temperature())
    sleep(1)
