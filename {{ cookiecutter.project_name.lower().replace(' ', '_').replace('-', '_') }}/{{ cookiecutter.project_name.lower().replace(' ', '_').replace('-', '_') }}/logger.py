from types import TracebackType

import logging
import sys

from rich.logging import RichHandler


def log_unexpected_exception(
    exc_type: type[BaseException], exc_value: BaseException, exc_traceback: TracebackType
):
    """Logs unexpected exceptions.

    Args:
        exc_type (type[BaseException]): exception type
        exc_value (BaseException): value of the exception
        exc_traceback (TracebackType): the traceback of the exception
    """
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    logger.critical("Uncaught exception!!", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = log_unexpected_exception

logger = logging.getLogger(__name__)

# the handler determines where the logs go: stdout/file
shell_handler = RichHandler(rich_tracebacks=True)
file_handler = logging.FileHandler("debug.log")

logger.setLevel(logging.DEBUG)
shell_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# the formatter determines what our logs will look like
fmt_shell = "%(message)s"
fmt_file = "%(levelname)-8s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"

shell_formatter = logging.Formatter(fmt_shell)
file_formatter = logging.Formatter(fmt_file)

# here we hook everything together
shell_handler.setFormatter(shell_formatter)
file_handler.setFormatter(file_formatter)

logger.addHandler(shell_handler)
logger.addHandler(file_handler)
