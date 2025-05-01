#!/usr/bin/env python3
import signal
from time import sleep as bekle


def main():
    while 1:
        bekle(0.5)
        print("wait...")
        if STOP:
            break


def sig_handle(num, hand):
    global STOP
    STOP = True
    print(signal.strsignal(signal.SIGTERM))  # Terminated.
    print("Term Signal detected...", num)
    # num termsig = 15


signal.signal(signal.SIGTERM, sig_handle)
STOP = False

if __name__ == "__main__":
    main()
