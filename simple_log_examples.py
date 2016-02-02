import simple_log as slog


# preconfigured with "DEBUG" level as default
# aligns the level names with proper identation
slog.debug("This is a debug message")
slog.warning("Something might be wrong")

# log any number and type of messages
class Bar(object):
    def __str__(self):
        return "a Bar"

slog.info(Bar(), 'on route', 22)

# use custom logger names or classes and and use levels as strings
class Foo(object):
    pass

log1 = slog.get_simple_logger('Some Big Name', 'INFO')
log2 = slog.get_simple_logger(Foo, 'ERROR')
log3 = slog.get_simple_logger('an unreasonably big name')
log1.info("The earth has", 1, 'moon(s)')
log2.critical('Everything blew up!')
log3.info('This will mess indentation up')


afile = "my_file.log"
log6 = slog.get_simple_logger("also-in-file1", logfile=afile)
log7 = slog.get_simple_logger("also-in-file2", logfile=afile)
log6.info("This will be printed in a file")
log7.info("This will also be printed in a file")


# avoid using levels in output

log4 = slog.get_simple_logger("No-level-logger", show_level=False)
log5 = slog.get_simple_logger("No-level-logger", show_level=False)
log4.info("<- no level there")
log5 = slog.get_simple_logger("Foobar", show_level=False)
log5.info("indentation still OK")
