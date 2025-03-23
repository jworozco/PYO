#!/usr/bin/python3
# This is a test of the pyo library
from pyo import *
from time import sleep

def main():
    s = Server().boot()
    # global volume control
    s.amp = 0.1

    # mul=0.1 will reduce the volume of each oscillator to 10% of the maximum
    freqs = [i*100+100 for i in range(8)]
    osc = Sine(freq=freqs, mul=0.1).out()
    osc.ctrl(title=f"Simple additive synthesis")

    s.gui(locals())

if __name__ == "__main__":
    main()



