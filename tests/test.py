import time
import random
import threading

def rand():
    i = random.randint(0, 999999)
    return i

def check():
    global a
    c = 0
    while c < 100:
        time.sleep(2)
        c = c + 1
        b = a
        print("b =", b)
        
def main():
    global a
    while True:
        while True:
            a = rand()
            print(a)
            time.sleep(5)
            return a

check_theread = threading.Thread(target=check())
check_theread.start()
main_thread = threading.Thread(target=main())
main_thread.start()


