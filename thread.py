import threading
import time

'''
def sum(a, b):
    print(a + b)

t = threading.Thread(target=sum, args=(3, 5))
t.start()

t = threading.Timer(3, sum, args=(3, 5))
t.start()
'''

def sum(a, b):
    print(a + b)
    time.sleep(10)

t = threading.Thread(target=sum, args=(3, 5))
t.setName("secondThread")
t.start()
print(threading.active_count())
print(threading.current_thread())
print(threading.enumerate())
t.join()
print("End of thread")