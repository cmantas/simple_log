import logging
from logging import *
from inspect import isclass
import sys


class SimpleManager(logging.Manager):
    """
    Overrides the getLogger method of logging.Manager in order to support any type of name
    """
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


class SimpleLogger (Logger):
    """
    Overrides logging.Logger methods: info, debug, etc, in order to support any count/type of messages.
    Does not support extra arguments apart from the messages in those methods.
    """
    def __init__(self, name, level=NOTSET):
        self.super = super(SimpleLogger, self) #avoid calling supper method all the time
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


################# HELPER METHODS  #################
# method joining an iterable into a single string
_s_join = lambda msgs: " ".join(map(str, msgs))


def _get_level_from_name(lname_or_val):
    """
    Lookup for the logging level, 'lname' and replace it with its actual value
    :param lname_or_val: the level name (string) or value(int)
    :return:
    """
    if isinstance(lname_or_val, basestring):
        # if input is string, try looking it up
        if lname_or_val in logging._levelNames:
            level = logging._levelNames[lname_or_val]
        else:
            raise Exception("I do not know that level: {}".format(lname_or_val))
        return level
    elif isinstance(lname_or_val, int):
        # it's not a name but a value: return itself
        return lname_or_val
    else:
        raise Exception("I cannot make a level of: {}".format(lname_or_val))


# ==========------> OVERWRITE logging DEFAULTS <-------=============== #
# overwrite root logger, logger class and manager, basic format
logging.BASIC_FORMAT='%(levelname)8s: %(message)s'
logging.root = SimpleLogger('root', level=DEBUG)
setLoggerClass(SimpleLogger)
Logger.manager = SimpleManager(logging.root)

# ===================> private, static params <======================== #
_name_size=15 # max name size allowed
_configured_loggers = set()


def get_simple_logger(name, level=INFO, show_level=True,logfile=None):
    """
    Creates and Returns a SimpleLogger instance.
    :param         name: The name of the logger (can be of any type)
    :param        level: The logging level (can be a string or int)
    :param   show_level: Whether to print level or not
    :param      logfile: The log filename (if any)
    :return: SimpleLogger instance
    """

    # get or create the logger
    new_logger = getLogger(name)

    # skip configuration if logger already configured
    if name in _configured_loggers:
        return new_logger
    else:
        _configured_loggers.add(name)

    # set logging level
    level = _get_level_from_name(level)
    new_logger.setLevel(DEBUG)

    # construct the console format
    console_format = '%(name){namesize}s: '.format(namesize=_name_size) if name else ""
    console_format += '%(message)s'
    if show_level: console_format = '[%(levelname)8s]' +console_format
    formatter = Formatter(console_format, "%b%d %H:%M:%S")

    # create a console handler
    console_handler = StreamHandler(sys.stderr)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)

    # add console handler
    new_logger.addHandler(console_handler)

    # disable propagating to loggers higher in logging hierarchy
    new_logger.propagate = False

    # create a different handler for logfile if any
    if logfile:
        file_handler = FileHandler(logfile)
        file_handler.setLevel(DEBUG)
        fformat = '%(asctime)-15s[%(levelname)5s] %(name)20s: %(message)s'
        fformatter = Formatter(fformat, "%b%d %H:%M:%S")
        file_handler.setFormatter(fformatter)
        new_logger.addHandler(file_handler)

    return new_logger





