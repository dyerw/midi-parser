import os
from bitstring import BitStream
from chunk import HeaderChunk, TrackChunk



# Path we're going to use while we're messing around
TMP_PATH = os.path.join('../test_midis', 'bonnie_tyler-total_eclipse_of_the_heart.mid')


class Midi(object):
    """
    This class represents an entire midi file.
    """

    def __init__(self, path):
        self.bit_stream = BitStream(open(path, "r"))
        self.chunks = self.chunkify(self.bit_stream)

    def chunkify(self, bit_stream, chunk_list=[]):
        """
        Turns a bit stream into a list of midi chunks.
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
        pass


# All the rest of this is just for testing stuff out
midi = Midi(TMP_PATH)

for chunk in midi.chunks:
    print chunk
    if chunk.chunk_id.bytes == 'MTrk':
        print len(chunk.events)
        print [chunk.events[i] for i in range(len(chunk.events[:50]))]

