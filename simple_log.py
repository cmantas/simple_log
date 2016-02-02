#from logging import *
#from logging import Manager

import logging_copy as logging
from logging_copy import *
from inspect import isclass

import sys


class SimpleManager(logging.Manager):
    def getLogger(self, name=None):

        # special handling for specific types of names
        if name:
            if isclass(name):
                name = name.__name__
            else:
                name = str(name)
            return super(SimpleManager, self).getLogger(name)
        else:
            return logging.root


def _s_join(msgs):
    return " ".join(map(str, msgs))


class SimpleLogger (Logger):

    def __init__(self, name, level=NOTSET):
        self.super = super(SimpleLogger, self)
        self.super.__init__(name, level)


    def info(self, *msgs):
        self.super.info(_s_join(msgs))

    def debug(self, *msgs):
        self.super.debug(_s_join(msgs))

    def warning(self, *msgs):
        self.super.warning(_s_join(msgs))

    def error(self, *msgs):
        self.super.error(_s_join(msgs))

    def exception(self, *msgs):
         self.super.exception(_s_join(msgs))

    def critical(self, *msgs):
        self.super.critical(_s_join(msgs))


def _get_level_from_name(lname):

    if isinstance(lname, basestring):
        if lname in logging._levelNames:
            level = logging._levelNames[lname]
        else:
            raise Exception("I do not know that level: {}".format(lname))
        return level
    elif isinstance(lname, int):
        return lname
    else:
        raise Exception("I cannot make a level of: {}".format(lname))



### overwrite root logger, logger class and manager, basic format
logging.BASIC_FORMAT='%(levelname)8s:%(message)s'
logging.root = SimpleLogger('root', level=DEBUG)
setLoggerClass(SimpleLogger)
Logger.manager = SimpleManager(logging.root)


_name_size=15 # max name size allowed
_configured_loggers = set()


def get_simple_logger(name, level=INFO, show_level=True, show_name=False, logfile=None):

    new_logger = getLogger(name)

    # skip configuration if already configured
    if name in _configured_loggers:
        return new_logger

    level = _get_level_from_name(level)
    new_logger.setLevel(DEBUG)

    console_handler = StreamHandler(sys.stderr)

    # construct console format
    console_format = '%(name){namesize}s: '.format(namesize=_name_size) if name else ""
    console_format += '%(message)s'
    if show_level: console_format = '[%(levelname)8s]' +console_format
    formatter = Formatter(console_format, "%b%d %H:%M:%S")

    # add console handler
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    new_logger.addHandler(console_handler)

    #Different handler for logfile
    if not logfile is None:
        file_handler = FileHandler(logfile)
        file_handler.setLevel(DEBUG)
        fformat = '%(asctime)-15s[%(levelname)5s] %(name)20s: %(message)s'
        fformatter = Formatter(fformat, "%b%d %H:%M:%S")
        file_handler.setFormatter(fformatter)
        #print "adding handler for %s" % logfile
        new_logger.addHandler(file_handler)

    new_logger.propagate = False
    #root.disabled = True
    _configured_loggers.add(name)
    return new_logger





