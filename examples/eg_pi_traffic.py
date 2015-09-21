# -*- coding: utf-8 -*-
# eg_pi_traffic.py

from recipes.pi_traffic import *

# Should this be imported?
red = Light('red')
amber = Light('amber')
green = Light('green')
from time import sleep

def log(n):
    print(
        '{n}: red is {red._state}, amber is {amber._state}, green is {green._state}'.format(
            red=red,
            amber=amber,
            green=green,
            n=n
        ))


#  Here is the essential lesson content.
log(1)
red.on()
log(2)

if True:
    red.on()
    log(3)
    amber.on()
    log(4)
    red.off()
    amber.off()
    green.on()
    log(5)
    green.off()
    amber.on()
    log(6)
    amber.off()
    red.on()
    log(7)
    




if __name__ == '__main__':
    print("Hi")

    # my_pi_traffic = PiTraffic()

