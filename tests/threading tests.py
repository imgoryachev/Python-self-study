import threading
import time

c = 100

def count20():
    a = 1
    global c
    while a < 21:
        print('a = ', a)
        if a == 10:
            c = 15
        time.sleep(1)
        a = a + 1

def count02():
    global c
    b = 1
    while b < c:
    #while a > 0:
        print('b = ', b)
        time.sleep(1)
        b = b + 1

inc = threading.Thread(target=count20)
dec = threading.Thread(target=count02)
inc.setName("incThread")
dec.setName("decThread")

inc.start()
dec.start()

#time.sleep(4)

#print(threading.enumerate())
# print(threading.active_count())

# count20()
# count02()