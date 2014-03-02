from bitstring import BitStream
from utils.bit_utils import read_variable_byte_data


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
        data_stream = BitStream(self.data)

        # First two bytes are the format type
        self.format_type = data_stream.read('bits:16')

        # Second two bytes are the number of tracks
        self.num_of_tracks = data_stream.read('bits:16')

        # Third two bytes are the time division
        self.time_division = data_stream.read('bits:16')

    def __repr__(self):
        return "%(super_repr)s %(format)d %(num_tracks)d %(time_div)d" % \
               {'super_repr': super(HeaderChunk, self).__repr__(),
                'format': self.format_type.int,
                'num_tracks': self.num_of_tracks.int,
                'time_div': self.time_division.int}


class TrackChunk(Chunk):
    def __init__(self, chunk_id, size, data):
        super(TrackChunk, self).__init__(chunk_id, size, data)

        self.events = self.eventify()

    def eventify(self):
        # TODO: figure out how to figure out length of data for diff event types

        # Each event starts with a variable byte delta time
        # delta_time = read_variable_byte_data(self.data)
        #
        # event_type = self.data.read('bits:8')

        return []