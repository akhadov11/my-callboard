from django.conf import settings

from datadog.threadstats import ThreadStats


class Statsd(object):

    def __init__(self):
        self.__dog = ThreadStats()

    def start(self, **kwargs):
        self.__dog.start(**kwargs)

    def flush(self):
        self.__dog.flush()

    def increment_counter(self, name, value=1):
        return self.__dog.increment(name, value, tags=[settings.ENV])

    def gauge(self, name, value):
        return self.__dog.gauge(name, value, tags=[settings.ENV])

    def get_timed(self, name):
        return self.__dog.timed(name, tags=[settings.ENV])


statsd = Statsd()
