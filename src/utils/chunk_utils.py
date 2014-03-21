from src.event import MidiChannelEvent, SystemExclusiveEvent, MetaEvent
from bit_utils import read_variable_byte_data
from src.event_types.midi_channel_event_types import *

CHANNEL_EVENT_LOOKUP = {'8': NoteOffEvent,
                        '9': NoteOnEvent,
                        'a': NoteAftertouchEvent,
                        'b': ControllerEvent,
                        'c': ProgramChangeEvent,
                        'd': ChannelAftertouchEvent,
                        'e': PitchBendEvent}


META_EVENT_LOOKUP = {'0': SequenceNumberEvent,
                     '1': TextEvent,
                     '2': CopyrightNoticeEvent}


def eventify(data):
        events = []

        last_event = None

        while data.pos < data.len:

            # Each event starts with a variable byte delta time
            delta_time = read_variable_byte_data(data)

            event_type = data.read('bits:8')

            # 0x00 to 0x7F are a continuation of the last event and are
            # actually data bytes
            if event_type.hex in [hex(i)[2:] for i in range(0, 128)] and last_event is not None:
                data.pos -= 8
                last_event.pos = 0
                events.append(get_midi_channel_event(delta_time, last_event, data))

            # 0x80 to 0xEF are Midi Channel Events
            # Decimal: 128 - 239
            elif event_type.hex in [hex(i)[2:] for i in range(128, 240)]:
                last_event = event_type
                events.append(get_midi_channel_event(delta_time, event_type, data))

            # 0xFF are Meta Events
            elif event_type.hex == 'ff':
                events.append(MetaEvent(delta_time, event_type, data))

            # 0xF0 and 0xF7 are System Exclusive Events
            elif event_type.hex in ['f0', 'f7']:
                events.append(SystemExclusiveEvent(delta_time, event_type, data))

            else:
                raise ValueError('%s is not a valid event type' % event_type.hex)

        return events


def get_midi_channel_event(delta_time, event_type, data):

    channel_event_type = event_type.read('bits:4')
    midi_channel = event_type.read('bits:4')

    channel_event_class = CHANNEL_EVENT_LOOKUP[channel_event_type.hex]

    return channel_event_class(delta_time, channel_event_type,
                               midi_channel, data)


def get_meta_channel_event(delta_time, event_type, data):

    meta_event_type = data.read('bits:8')

    meta_event_class = META_EVENT_LOOKUP[meta_event_type.hex]

    return meta_event_class(delta_time, event_type, meta_event_type, data)



