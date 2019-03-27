from threading import Thread
import time


class A(Thread):

    def __init__(self, an):
        Thread.__init__(self)
        self.an = an

    def run(self):
        print("Firul: {}; ".format(self.an), end="\n.»")
        time.sleep(1)


print("Se executa Threadurile", end="\n")
for i in range(5):
    t = A(i)
    t.setDaemon(True)
    t.start()
time.sleep(5)
t.join()
print("\nExecutie threaduri terminata!")
