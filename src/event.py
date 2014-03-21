from src.utils.bit_utils import read_variable_byte_data


class Event(object):
    def __init__(self, delta_time, event_type_value):
        self.delta_time = delta_time.int
        self.event_type_value = event_type_value.hex

    def __repr__(self):
        return "%d %s" % (self.delta_time, self.event_type_value)


class MidiChannelEvent(Event):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(MidiChannelEvent, self).__init__(delta_time,
                                               channel_event_type + midi_channel)

        self.channel_event_type = channel_event_type

        self.midi_channel = midi_channel

        self._parameter_1 = event_data.read('bits:8')

        if self.channel_event_type.hex not in ['c', 'd']:
            self._parameter_2 = event_data.read('bits:8')


class MetaEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(MetaEvent, self).__init__(delta_time, event_type_value, )

        self.meta_event_type = event_data.read('bits:8')

        #self.data_length = read_variable_byte_data(data_bit_stream)
        self.data_length = event_data.read('bits:8')

        self.data = event_data.read('bits:%d' % (8*self.data_length.int))


class SystemExclusiveEvent(Event):
    def __init__(self, delta_time, event_type_value, event_data):
        super(SystemExclusiveEvent, self).__init__(delta_time, event_type_value)

        self.data_length = read_variable_byte_data(event_data)

        self.data = event_data.read('bits:%d' % (8*self.data_length.int))