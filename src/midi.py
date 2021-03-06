import os
from bitstring import BitStream, BitArray
from chunk import HeaderChunk, TrackChunk


class Midi(object):
    """
    This class represents an entire midi file, comprising of a list of :class:`Chunk`s.
    """

    def __init__(self, path):
        self.bit_stream = BitStream(open(path, "r"))
        chunks = self.chunkify(self.bit_stream)
        self.header = chunks[0]
        self.tracks = chunks[1:]

    def chunkify(self, bit_stream, chunk_list=[]):
        """
        Takes a bit_stream representing the data for a midi file and parses it
        into a list of :class:`Chunk` objects.

        :param BitStream bit_stream: The BitStream taken from the data of the midi file.
        :returns list: A list of :class:`Chunk` representing the data chunks in the midi file.
        """

        # If this is the end of the bitstream return the chunk list
        if bit_stream.pos == bit_stream.length:
            return chunk_list

        # First four bytes are the chunk id
        chunk_id = bit_stream.read('bits:32')

        # Next four bytes are the chunk size (in bytes)
        chunk_size = bit_stream.read('bits:32')

        # The rest of the chunk is chunk specific data
        chunk_data = bit_stream.read('bits:%d' % (chunk_size.int*8))

        # If the chunk id matches MThd, it is a HeaderChunk
        if chunk_id.bytes == 'MThd':
            chunk_list.append(HeaderChunk(chunk_id, chunk_size, chunk_data))
            return self.chunkify(bit_stream, chunk_list=chunk_list)

        # If the chunk id matched MTrk, it is a TrackChunk
        elif chunk_id.bytes == 'MTrk':
            chunk_list.append(TrackChunk(chunk_id, chunk_size, chunk_data))
            return self.chunkify(bit_stream, chunk_list=chunk_list)

        # Midis only contain header and track chunks
        else:
            raise ValueError('Didn\'t recognize chunk id: %s' % chunk_id.bytes)

    def write(self, path):
        with open(path, 'w') as f:
            for chunk in self.chunks:
                f.write(chunk.get_bytes())




