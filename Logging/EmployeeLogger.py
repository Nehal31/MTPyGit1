import logging

LogFile = 'EmployeeLog'
LogFileMode = 'a+'
LoggerName = __name__
LogLevel = logging.DEBUG
LogFormat = '%(asctime)s %(filename)s %(**%(levelname)s** %(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(LogLevel)

formatter = logging.Formatter(LogFormat)

handler = logging.FileHandler(LogFile)
handler.setFormatter(formatter)

logger.addHandler(handler)


class Employee:
    def __init__(self, eid, name):
        self.eid = eid
        self.name = name

        logger.info("Created new Employee : Name : {} Employee Id : {}".format(self.name, self.eid))


def main():
    emp1 = Employee('Nehal', 'IBE1117')
    emp2 = Employee('Kumar', 'IBE1118')

    print(emp1)
    print(emp2)


if __name__ == '__main__':
    main()