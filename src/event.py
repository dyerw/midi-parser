from bitstring import Bits, BitStream
from utils.bit_utils import read_variable_byte_data


class Event(object):
    def __init__(self, delta_time, event_type_value, event_data):
        self.delta_time = delta_time
        self.event_type_value = event_type_value
        self.event_data = event_data


class MidiChannelEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(MidiChannelEvent, self).__init__(delta_time, event_type_value, event_data)
        data_bit_stream = BitStream(self.event_data)

        self.midi_channel = data_bit_stream.read('bits:4')

        self.parameter_1 = data_bit_stream.read('bits:8')

        self.parameter_2 = data_bit_stream.read('bits:8')


class MetaEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(MetaEvent, self).__init__(delta_time, event_type_value, event_data)
        data_bit_stream = BitStream(self.event_data)

        self.meta_event_type = data_bit_stream.read('bits:8')

        self.data_length = read_variable_byte_data(data_bit_stream)

        self.data = data_bit_stream.read('bits:%d' % (8*self.data_length.int))


class SystemExclusiveEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(SystemExclusiveEvent, self).__init__(delta_time, event_type_value, event_data)
        data_bit_stream = BitStream(self.event_data)

        self.data_length = read_variable_byte_data(data_bit_stream)

        self.data = data_bit_stream.read('bits:%d' % (8*self.data_length.int))