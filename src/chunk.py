from bitstring import BitStream, Bits

from src.utils.chunk_utils import eventify


class Chunk(object):
    """
    This class represents a chunk of any sort found in a midi file.
    :class:`HeaderChunk` and :class:`TrackChunk` inherit from this class, it
    is never initialized directly.
    """

    def __init__(self, chunk_id, size):
        self.chunk_id = chunk_id.bytes
        self.chunk_size = size.int

    def __repr__(self):
        return self.chunk_id

    def get_bytes(self):
        pass


class HeaderChunk(Chunk):
    """
    Represents the header chunk of a midi file. Each midi object only has one
    header chunk. The header chunk contains information that pertains to the track as a whole.
    """
    def __init__(self, chunk_id, size, data):
        super(HeaderChunk, self).__init__(chunk_id, size)
        data_stream = BitStream(data)

        # First two bytes are the format type
        self.format_type = data_stream.read('bits:16').int

        # Second two bytes are the number of tracks
        self.num_of_tracks = data_stream.read('bits:16').int

        # Third two bytes are the time division
        self.time_division = Bits(data_stream.read('bits:16'))

    def __repr__(self):
        return "%(super_repr)s %(format)d %(num_tracks)d %(time_div)d" % \
               {'super_repr': super(HeaderChunk, self).__repr__(),
                'format': self.format_type.int,
                'num_tracks': self.num_of_tracks.int,
                'time_div': self.time_division.int}


class TrackChunk(Chunk):
    def __init__(self, chunk_id, size, data):
        super(TrackChunk, self).__init__(chunk_id, size)

        self.events = eventify(data)