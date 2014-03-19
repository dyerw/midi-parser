from src.event import MidiChannelEvent, SystemExclusiveEvent, MetaEvent
from bit_utils import read_variable_byte_data


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
                events.append(MidiChannelEvent(delta_time, last_event, data))

            # 0x80 to 0xEF are Midi Channel Events
            # Decimal: 128 - 239
            elif event_type.hex in [hex(i)[2:] for i in range(128, 240)]:
                last_event = event_type
                events.append(MidiChannelEvent(delta_time, event_type, data))

            # 0xFF are Meta Events
            elif event_type.hex == 'ff':
                events.append(MetaEvent(delta_time, event_type, data))

            # 0xF0 and 0xF7 are System Exclusive Events
            elif event_type.hex in ['f0', 'f7']:
                events.append(SystemExclusiveEvent(delta_time, event_type, data))

            else:
                raise ValueError('%s is not a valid event type' % event_type.hex)

        return events