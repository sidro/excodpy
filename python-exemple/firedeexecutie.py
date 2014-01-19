from threading import Thread
import time
import random


class A(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        self.a = a

    def run(self):
        time.sleep(1)
        print("Firul: {}".format(self.a))


print("Se executa Threadurile\n")
for i in range(5):
    t = A(i)
    t.setDaemon(True)
    t.start()
time.sleep(4)
t.join()
print("\nExecutie threaduri terminata!\n")
