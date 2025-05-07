class Gauge(object):
    def __init__(self, max_value):
        self.current = max_value
        self.max = max_value

    def reset(self):
        self.current = self.max
