from bitstring import Bits


class Event(object):
    def __init__(self, bits):
        self.delta_time = None
        self.event_type_value = None