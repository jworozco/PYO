#!/usr/bin/python3
# This is a test of the pyo library
from pyo import *
from time import sleep

def main():
    s = Server().boot()
    # modulator oscillator
    mod = Sine(freq=205, mul=500, add=200)
    # carrier oscillator
    car = Sine(freq=mod, mul=0.2).out()
    s.gui(locals())

    # using the interpreter it is possible to change the frequency of the modulator interactively, for exaple:
    # mod.freq = 205

if __name__ == "__main__":
    main()



