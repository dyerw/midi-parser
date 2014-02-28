from bitstring import Bits


class Chunk(object):
    """
    This class represents a chunk of any sort found in a midi file.
    """

    def __init__(self, bits):
        self.id = bits[:4*8]
        self.size = bits[4*8:8*8]
        self.data = bits[8*8:]

    def __repr__(self):
        return self.id.bytes + ' ' + str(self.size.int)


class HeaderChunk(Chunk):
    def __init__(self, bits):
        super(HeaderChunk, self).__init__(bits)

        self.format_type = self.data[:2*8]
        self.num_of_tracks = self.data[2*8:4*8]
        self.time_division = self.data[4*8:]

    def __repr__(self):
        return super(HeaderChunk, self).__repr__() + " " + str(self.format_type.int) + " " + str(self.num_of_tracks.int) + " " + str(self.time_division.int)


class TrackChunk(Chunk):
    def __init__(self, bits):
        super(TrackChunk, self).__init__(bits)

        self.events = self.eventify(self.data)

    def eventify(self, bits):
        return []