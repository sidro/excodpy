from threading import Thread
import time
import random


class A(Thread):
    def __init__(self, a):
        Thread.__init__(self)
        self.a = a

    def run(self):
        time.sleep(random.randint(1,10))
        print("Firul: {}".format(self.a))



for i in range(5):
    t = A(i)
    t.setDaemon(True)
    t.start()
t.join()
