#!/usr/bin/python3
# This is a test of the pyo library
from pyo import *
from time import sleep

def main():
    s = Server().boot()
    # global volume control
    s.amp = 0.1

    # mul=0.1 will reduce the volume of each oscillator to 10% of the maximum
    # i%2 will alternate between 0 and 1 and so it will alternate between the left and right channels
    # each oscillator will be assigned to a different window
    osc = [Sine(freq=(i*100+100), mul=0.1).out(i%2) for i in range(8)]
    for i in range(8):
        osc[i].ctrl(title=f"Simple additive synthesis {i}")

    print(locals())
    s.gui(locals())

if __name__ == "__main__":
    main()



