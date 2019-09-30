from time import time,sleep

class my_math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ready = False
        self.safe = False
        sleep(1)

    def set_ready(self):
        self.ready = True
        sleep(1)

    def set_safe_state(self):
        self.safe = True
        sleep(1)

    def set_notready(self):
        self.ready = False
        sleep(1)

    def set_unsafe_state(self):
        self.safe = False
        sleep(1)

    #@status
    def add(self):
        if not self.ready:
            print("Not Ready")
            return None
        return self.a + self.b

    #@status
    def div(self):
        if not self.ready:
            print("Not Ready")
            return None
        if self.b == 0:
            if self.safe:
                print("Safe Sate Policy Active. Divisor can't be 0")
                return None
            else:
                print("Safe Sate Policy not Active. Divisor can be 0")
        return self.a / self.b



"""
    def status(self, func):
        def inner(self):
            
            self.func()
        return inner()
"""