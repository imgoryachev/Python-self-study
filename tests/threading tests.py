import threading
import time

def count20():
    a = 1
    while a < 21:
        print(a)
        time.sleep(1)
        a = a + 1

def count02():
    a = 20
    while a > 0:
        print(a)
        time.sleep(1)
        a = a - 1

inc = threading.Thread(target=count20)
dec = threading.Thread(target=count02)
inc.setName("incThread")
dec.setName("decThread")

inc.start()
dec.start()

time.sleep(4)

print(threading.enumerate())
# print(threading.active_count())

# count20()
# count02()