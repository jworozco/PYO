#!/usr/bin/python3
# This is a test of the pyo library
from pyo import *
from time import sleep

def main():
    s = Server().boot()
    #global volume control
    s.amp = 0.1

    #mul=0.1 will reduce the volume of each oscillator to 10% of the maximum
    #the list of frequencies will be displayed as a list of sliders
    osc = Sine([100, 200, 300, 400, 500, 600, 700, 800], mul=0.1).out()
    osc.ctrl(title="Simple additive synthesis")

    s.gui(locals())
    print("Goodbye, World!")

if __name__ == "__main__":
    main()



