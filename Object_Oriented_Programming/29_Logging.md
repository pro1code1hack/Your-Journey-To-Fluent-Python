# Logging

_Logging is a technique for monitoring events that take place when some software is in use. For the creation, operation,
and debugging of software, logging is crucial. There are extremely little odds that you would find the source of the
issue if your software fails and you don't have any logging records._

_A built-in Python package called logging enables publishing status messages to files or other output streams.
The file may provide details about which portion of the code is run and any issues that have come up._

### Loging levels:

+ **Debug**: These are used to provide detailed information, which is usually only relevant when identifying issues.
+ **Information**: These are used to verify that everything is functioning as planned.
+ **Warning**:These are utilized as a sign that something unexpected happened or as a sign that there may be an issue
  soon.
+ **Error**: This indicates that the software was unable to complete a task because of a more serious issue.
+ **Critical**: This indicates a major mistake that may prevent the application from continuing to execute.

_Each level's associated methods are accessible by calling_

+ Example:

```python
import logging

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
```

### Basic Configurations

_You set up the logging, use the basicConfig(**kwargs) function._

+ Make the logger and configure it. It may include a number of parameters. Passing the file name into the program is
  crucial if you wish to record the occurrences.
+ Here, the logger's format may also be modified. The file operates in append mode by default, but we may switch to
  write mode if necessary.
+ Additionally, the logger's level, which determines the tracking threshold depending on the numerical values provided
  to each level, may be adjusted.

+ Example:

```python
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
```

### Creating Formatted Output

_While you can pass any variable that can be represented as a string from your program as a message to your logs, there
are some basic elements that are already a part of the LogRecord and can be easily added to the output format.
If you want to log the process ID along with the level and message_

+ Example:

```python
import logging

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
```

### Classes and Functions

_We have seen the root default logger so far, which is utilized anytime the logging module's methods are explicitly
invoked, like this: logging.debug (). If your application has many modules, you may (and should) define your own logger
by making an object of the Logger class. Examining a few of the classes and functions in the module will help._

_Logging module:_

+ Logger: This is the class whose objects will be utilized directly to call methods in the application code.

+ LogRecord: The name of the logger, the function, the line number, the message, and other details are all included in
  the LogRecord objects that loggers automatically produce.

+ Handler: Handlers transmit the LogRecord to the necessary output location, such as a file or the console. Subclasses
  like StreamHandler, FileHandler, SMTPHandler, HTTPHandler, and others derive from the base class Handler. These
  subclasses transmit the logging outputs to the appropriate locations, such as a disk file or sys.stdout.

+ Formatter: Here, you may specify the output's format by providing a string format that identifies the properties it
  should include.

+ Example:

```python
import logging

logger = logging.getLogger('example')
logger.warning('warning')
```

### Handlers

_When you wish to customize your own loggers and transmit the created logs to other locations, handlers come into play.
Handlers transmit the log messages to predetermined locations, such as a file or the standard output stream._

_Similar to logs, handlers allow you to choose the severity level. This is helpful if you want to establish various
severity levels for each handler while using the same logger._

+ Example:

```python
import logging

from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
LOG_FILE = "my_app.log"


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)  # better to have too much log than not enough

    # with this pattern, it's rarely necessary to propagate the error up to parent
    logger.propagate = False
    return logger
```