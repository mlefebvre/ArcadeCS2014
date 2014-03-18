from threading import Thread
import time
import sys, signal

DRINK_TIME = 1000

class Pump(Thread):
    running = True
    opened = False
    open_time = 0

    def __init__(self, port):
        Thread.__init__(self)
        self.port = port
        self.daemon = True
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signal, frame):
        self.close()
        sys.exit(0)

    def run(self):
        while(self.running):
            print "aaa"
            time.sleep(1)

    def kill(self):
        self.running = False

    def drink(self):
        self.opened = True
        self.open_time = time.time()
        print "OPEN"

    def close(self):
        print "CLOSE"