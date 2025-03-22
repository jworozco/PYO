#!/usr/bin/python3
# This is a test of the pyo library
from pyo import *
from time import sleep

s = Server().boot()
s.start()

a = Sine(freq=440.0, mul=0.2).out()

def main():
    sleep(5)
    print("Goodbye, World!")

if __name__ == "__main__":
    main()



