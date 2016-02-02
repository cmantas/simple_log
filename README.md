Simple Log for Python
=====================

simple_log provides is a simplistic wrapper for python logging module.
It is supposed to be used as a drop in replacement for "print" for people who cannot 
be bothered to set up proper logging. 

It allows logging for any type and count of messages but sacrifices being able to parse arguments.
Its functions are NOT interchangable with those in the logging module but follow a close resemblance.


Basic
------
simple_log can be used withoud defining a logger object.
By default it's configured in a 'DEBUG' level.
In this case it alligns the level names

```python
import simple_log as slog

slog.debug("This is a debug message")
slog.warning("Something might be wrong")

>   DEBUG:This is a debug message
> WARNING:Something might be wrong
```

