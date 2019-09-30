import logging as log

logger = log.getLogger("")
logger.setLevel(log.INFO)

format = "%(asctime)s %(filename)s %(levelname)s %(message)s"
datefmt = "%Y %b %d %H:%M:%S"

formatter = log.Formatter(format, datefmt=datefmt)

handler = log.FileHandler(filename='mylog.log', mode='w')
handler.setFormatter(formatter)
handler.setLevel(log.INFO)


logger.addHandler(handler)

class LogTest:

    def __init__(self):
        self.log = logger

    def log_somthing(self):
        self.log.info("Logging Something")



class LogTest2:
    def __init__(self):
        self.log = log
        self.log.basicConfig(filename='mylog.log', filemode='w', level=log.INFO )
        print(self.log)


    def log_somthing(self):
        self.log.info("Logging Something logtest2")



lt = LogTest()
lt.log_somthing()

lt = LogTest2()
lt.log_somthing()