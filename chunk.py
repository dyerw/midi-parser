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


class TrackChunk(Chunk):
    def __init__(self, bits):
        super(TrackChunk, self).__init__(bits)