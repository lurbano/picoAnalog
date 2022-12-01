import board
import neopixel
import time
from analogio import AnalogIn
from ledPixelsPico import *

nPix = 20

ledPix = ledPixels(nPix, board.GP0)

potR = AnalogIn(board.A2)
potG = AnalogIn(board.A1)
potB = AnalogIn(board.A0)
pmin = 200
pmax = 65600

def colVal(v):
    return int(((v - pmin) / pmax) * 255)

while True:
    r = colVal(potR.value)
    g = colVal(potG.value)
    b = colVal(potB.value)
    print(r, g, b)
    ledPix.setColor((r, g, b))
    time.sleep(0.25)