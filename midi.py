from bitstring import BitArray, Bits
from data.constants import CHUNK_ID_TO_CLASS
import os


# Path we're going to use while we're messing around
TMP_PATH = os.path.join('test_midis', 'bonnie_tyler-total_eclipse_of_the_heart.mid')


class Midi(object):
    """
    This class represents an entire midi file.
    """

    def __init__(self, path):
        self.bits = Bits(open(path, "r"))
        self.chunks = self.chunkify(self.bits)

    def chunkify(self, bits):
        if len(bits) == 0:
            return []

        # number of bytes in the first chunk as number of bytes
        first_chunk_size = bits[4*8:8*8].int

        # this is the total size of the first chunk including chunk id and size
        split_ind = 8 + first_chunk_size

        return [CHUNK_ID_TO_CLASS[bits[:4*8].bytes](bits[:split_ind*8])] + self.chunkify(bits[split_ind*8:])


# All the rest of this is just for testing stuff out
midi = Midi(TMP_PATH)

for chunk in midi.chunks:
    print chunk

