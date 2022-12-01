import board
import neopixel
import time
from analogio import AnalogIn

nPix = 20
pixels = neopixel.NeoPixel(board.GP0, nPix)


potR = AnalogIn(board.A2)
potG = AnalogIn(board.A1)
potB = AnalogIn(board.A0)
pmin = 200
pmax = 65600

def colVal(v):
    return int(((v - pmin) / pmax) * 255)

while True:
    pR = potR.value
    pG = potG.value

    r = colVal(potR.value)
    g = colVal(potG.value)
    b = colVal(potB.value)
    print(r, g, b)
    pixels[0] = (r, g, b)
    time.sleep(0.25)