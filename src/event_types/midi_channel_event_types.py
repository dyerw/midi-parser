from src.event import MidiChannelEvent


class NoteOffEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(NoteOffEvent, self).__init__(delta_time, channel_event_type,
                                           midi_channel, event_data)

        self.note_number = self._parameter_1
        self.velocity = self._parameter_2


class NoteOnEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(NoteOnEvent, self).__init__(delta_time, channel_event_type,
                                          midi_channel, event_data)

        self.note_number = self._parameter_1
        self.velocity = self._parameter_2


class NoteAftertouchEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(NoteAftertouchEvent, self).__init__(delta_time, channel_event_type,
                                                  midi_channel, event_data)

        self.note_number = self._parameter_1
        self.aftertouch_value = self._parameter_2


class ControllerEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(ControllerEvent, self).__init__(delta_time, channel_event_type,
                                              midi_channel, event_data)

        self.controller_number = self._parameter_1
        self.controller_value = self._parameter_2


class ProgramChangeEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(ProgramChangeEvent, self).__init__(delta_time, channel_event_type,
                                                 midi_channel, event_data)

        self.program_number = self._parameter_1


class ChannelAftertouchEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(ChannelAftertouchEvent, self).__init__(delta_time,
                                                     channel_event_type,
                                                     midi_channel, event_data)

        self.aftertouch_value = self._parameter_1


class PitchBendEvent(MidiChannelEvent):
    def __init__(self, delta_time, channel_event_type, midi_channel, event_data):
        super(PitchBendEvent, self).__init__(delta_time, channel_event_type,
                                             midi_channel, event_data)

        self.pitch_value_lsb = self._parameter_1
        self.pitch_value_msb = self._parameter_2
