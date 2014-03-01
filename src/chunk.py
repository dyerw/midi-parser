from bitstring import Bits


class Chunk(object):
    """
    This class represents a chunk of any sort found in a midi file.
    """

    def __init__(self, chunk_id, size, data):
        self.chunk_id = chunk_id
        self.size = size
        self.data = data

    def __repr__(self):
        return self.chunk_id.bytes + ' ' + str(self.size.int)


class HeaderChunk(Chunk):
    def __init__(self, chunk_id, size, data):
        super(HeaderChunk, self).__init__(chunk_id, size, data)

        self.format_type = self.data[:2*8]
        self.num_of_tracks = self.data[2*8:4*8]
        self.time_division = self.data[4*8:]

    def __repr__(self):
        return "%(super_repr)s %(format)d %(num_tracks)d %(time_div)d" % \
               {'super_repr': super(HeaderChunk, self).__repr__(),
                'format': self.format_type.int,
                'num_tracks': self.num_of_tracks.int,
                'time_div': self.time_division.int}


class TrackChunk(Chunk):
    def __init__(self, chunk_id, size, data):
        super(TrackChunk, self).__init__(chunk_id, size, data)

        self.events = self.eventify(self.data)

    def eventify(self, chunk_data):
        return []