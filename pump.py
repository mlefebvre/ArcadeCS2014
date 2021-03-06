from threading import Thread, Lock
import time
import sys
import signal
import serial

DRINK_TIME = 1
ON_STRING = "e"
OFF_STRING = "o"


class Pump(Thread):
    running = True
    opened = False
    close_time = 0
    ser = None

    def __init__(self, port):
        Thread.__init__(self)
        self.daemon = True
        self.lock = Lock()
        self.port = port
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, signal, frame):
        self.close()
        sys.exit(0)

    def run(self):
        while self.running:
            if self.opened and time.time() > self.close_time:
                self.opened = False
                self.close()
            time.sleep(0.01)

    def kill(self):
        self.running = False

    def drink(self):
        if self.opened:
            self.close_time += DRINK_TIME
        else:
            self.opened = True
            self.close_time = time.time() + DRINK_TIME
            self._send_command(ON_STRING)

    def close(self):
        self._send_command(OFF_STRING)

    def _send_command(self, command):
        with self.lock:
            if self.ser:
                self.ser.write(command)
            else:
                print command

    def __enter__(self):
        try:
            print "Opening serial port"
            self.ser = serial.Serial(self.port, 19200)
        except Exception as e:
            print e
            self.ser = None

    def __exit__(self, type, value, traceback):

        if self.ser:
            self.kill()
            self.join(5)
            self.close()
            print "Closing serial port"
            self.ser.close()
