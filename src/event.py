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

        #self.midi_channel = self.event_data.read('bits:4')
        self.channel_event_type = event_type_value.read('bits:4')

        self.midi_channel = event_type_value.read('bits:4')

        print self.channel_event_type.hex
        print self.midi_channel.hex

        self.parameter_1 = self.event_data.read('bits:8')

        if self.channel_event_type.hex not in ['c', 'd']:
            self.parameter_2 = self.event_data.read('bits:8')


class MetaEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(MetaEvent, self).__init__(delta_time, event_type_value, event_data)

        self.meta_event_type = self.event_data.read('bits:8')

        #self.data_length = read_variable_byte_data(data_bit_stream)
        self.data_length = self.event_data.read('bits:8')

        self.data = self.event_data.read('bits:%d' % (8*self.data_length.int))


class SystemExclusiveEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(SystemExclusiveEvent, self).__init__(delta_time, event_type_value, event_data)

        self.data_length = read_variable_byte_data(self.event_data)

        self.data = self.event_data.read('bits:%d' % (8*self.data_length.int))