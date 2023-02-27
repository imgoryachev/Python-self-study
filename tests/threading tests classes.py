import threading
import time
import keyboard

keyboard.read_event
check = True

class asd(threading.Thread):

    def run(self):
        a = 1
        while check:
            print(a)
            time.sleep(1)
            a = a + 1

a = asd()
a.start()

class Fish(threading.Thread):

    def ping():
        a = 1
        while a <= 4:
            print(a)
            time.sleep(1)
            a = a + 1


fish = threading.Thread(target=Fish.ping)
fish.start()
fish.join()
check = False
