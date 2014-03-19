from src.event import MidiChannelEvent


class NoteOffEvent(MidiChannelEvent):

    def __init__(self, note_number, velocity):
        super(NoteOffEvent, self).__init__()

        self.note_number = note_number
        self.velocity = velocity

