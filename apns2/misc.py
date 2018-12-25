import logging


class LoggerAdapter(logging.LoggerAdapter):
    """
    An adapter for loggers which makes it easier to specify contextual
    information in logging output.
    """

    def process(self, msg, kwargs):
        """
        Process the logging message and keyword arguments passed in to
        a logging call to insert contextual information. You can either
        manipulate the message itself, the keyword args or both. Return
        the message and kwargs modified (or not) to suit your needs.
        Normally, you'll only need to override this one method in a
        LoggerAdapter subclass for your specific needs.
        """
        kwargs["extra"] = dict(self.extra, **(kwargs["extra"] or {}))
        return msg, kwargs
