#!/usr/bin/env python
import signal
import threading
from time import sleep as bekle


def main():
    # sinyaller = signal.valid_signals()
    # sistemde desteklenen sinyalleri ekrana basıyoruz.
    # for i in sinyaller:
    #     print(i)
    kanal1 = threading.Thread(target=sayac, args=(0.2,))
    kanal1.start()
    kanal1.join()
    while 1:
        if kanal1.is_alive():
            bekle(0.1)
        else:
            break
    print("bitti")  # system çıkış kodu ekrana basılır.


def sayac(sure):
    global ABORT
    while 1:
        if not ABORT:
            for i in range(1, 10):
                bekle(sure)
                if ABORT:
                    break
                print(i)
        bekle(1)
        print("devam etmesi için sinyal bekleniyor...")


def sinyal_yakala(num, hand):
    print("Abort Signal", num, hand)
    global ABORT
    if num == 6:
        ABORT = True
    elif num == 18:
        ABORT = False
    else:
        pass


signal.signal(signal.SIGABRT, sinyal_yakala)  # abort signal yapılan işlemi iptal eder
signal.signal(signal.SIGCONT, sinyal_yakala)  # cont signal yapılan işleme devam eder
#  kill -6 abort için kill -18 devam ettirmek için

ABORT = False


if __name__ == "__main__":
    main()
