import datetime
from os import path
import logging as log


# get path to utils.py
def get_path():
    return path.dirname(path.abspath(__file__))


# --------------------------------------------------- LOGS -------------------------------------------------------------
'''
    documentation:
    https://docs.python.org/3/howto/log.html

    article on logging simultainously to file and console
    https://stackoverflow.com/questions/9321741/printing-to-screen-and-writing-to-a-file-at-the-same-time
'''

# set up log to file
# regex: ^(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s-\s(\S*)\s*-\s(\S*)\s*-\s([A-Z]{4,7})\s*(.*)$	^\d	%Y-%m-%d %H:%M:%S
log.basicConfig(filename=path.join(get_path(), 'data', 'log.log'),
                filemode='a',
                format='%(asctime)s - %(threadName)-12s - %(name)-25s - %(levelname)-8s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                level=log.DEBUG
                )

# define a Handler which writes INFO messages or higher to the sys.stderr
console = log.StreamHandler()
console.setLevel(log.INFO)
# set a format which is simpler for console use
formatter = log.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
log.getLogger('').addHandler(console)


# --------------------------------------------------- UTILS ------------------------------------------------------------
class Timer:
    def __init__(self):
        self.start_dt = None

    def start(self):
        self.start_dt = datetime.datetime.now()

    def stop(self):
        end_dt = datetime.datetime.now()
        log.info('[Utils    ]: time taken: %s' % (end_dt - self.start_dt))
