import logging as log

logger = log.getLogger('')
logger.setLevel(log.DEBUG)

#format = '%(asctime)s %(funcName)s %(lineno)s **%(levelname)s** %(message)s'
format = '%(asctime)s %(levelname)s %(message)s'
formater = log.Formatter(format)


handler = log.FileHandler('mylog.log')
handler.setLevel(log.DEBUG)
handler.setFormatter(formater)

logger.addHandler(handler)
