Simple Log for Python
=====================

simple_log provides is a simplistic wrapper for python logging module.
It is supposed to be used as a drop in replacement for "print" for people who cannot 
be bothered to set up proper logging. 

It allows logging for any type and count of messages but sacrifices being able to parse arguments.
Its functions are NOT interchangable with those in the logging module but follow a close resemblance.


Basic
------
simple_log can be used withoud creating a logger object.

By default it's configured in a 'DEBUG' level and no logger name is printed.

In this case it alligns the level names

```python
import simple_log as slog

slog.debug("This is a debug message")
slog.warning("Something might be wrong")

>   DEBUG: This is a debug message
> WARNING: Something might be wrong
```

Any Arguments
--------------
Any number of arguments is converted to a joined string message.
```python
class Bar(object):
    def __str__(self):
        return "a Bar"

slog.info(Bar(), 'on route', 22)

>    INFO: a Bar on route 22
```

Custom Names or Classes
-----------------------
You can use custom logger names or classes instead of names.

You can also use levels as strings.

```python
class Foo(object):
    pass

log1 = slog.get_simple_logger('Some Big Name', 'INFO')
log2 = slog.get_simple_logger(Foo, 'ERROR')
log3 = slog.get_simple_logger('an unreasonably big name')
log1.info("The earth has", 1, 'moon(s)')
log2.critical('Everything blew up!')
log3.info('Indentation is messed up by big names)

>[    INFO]  Some Big Name: The earth has 1 moon(s)
>[CRITICAL]            Foo: Everything blew up!
>[    INFO]an unreasonably big name: This will mess indentation up
```

File Logging (experimental)
-------------------
By defining a filename, the the logger will also print to a file.

The loggin level of file output is fixed to 'DEBUG' (for now).

The output format is also fixed

```python
afile = "my_file.log"
log6  = slog.get_simple_logger("also-in-file1", logfile=afile)
log7  = slog.get_simple_logger("also-in-file2", logfile=afile)
log6.info("This will be printed in a file")
log7.info("This will also be printed in a file")

>[    INFO]  also-in-file1: This will be printed in a file
>[    INFO]  also-in-file2: This will also be printed in a file

```
in file 'my_file.log':
```
Jan22 17:56:05 [ INFO]        also-in-file1: This will be printed in a file
Jan22 17:56:05 [ INFO]        also-in-file2: This will also be printed in a file
```

Misc
-----
No Levels
*********
You can also avoid printing levels in output

```python
log4 = slog.get_simple_logger("No-level-logger", show_level=False)
log5 = slog.get_simple_logger("No-level-logger", show_level=False)
log4.info("<- no level there")
log5 = slog.get_simple_logger("Foobar", show_level=False)
log5.info("indentation still OK")

>No-level-logger: <- no level there
>         Foobar: indentation still OK
```
