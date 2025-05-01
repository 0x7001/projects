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
    if kanal1.is_alive():
        bekle(0.1)

    print("bitti")  # system çıkış kodu ekrana basılır.


def sayac(sure):
    for i in range(1, 10):
        bekle(sure)
        if STOP:
            break
        print(i)


def sinyal_yakala(num, hand):
    print("ben öldüm...", num, hand)
    global STOP
    STOP = True


signal.signal(signal.SIGINT, sinyal_yakala)
# sinyalleri yakalamak için SIGINT yakalanınca global değişken değişecek
# ctrl+c ile sigint
STOP = False


if __name__ == "__main__":
    main()
