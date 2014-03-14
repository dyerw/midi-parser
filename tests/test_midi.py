import unittest
import os
from bitstring import BitArray
from src.midi import Midi


class TestMidi(unittest.TestCase):
    def setUp(self):
        pass

    def test_write_out_valid_midi(self):
        data_path = os.path.join('data', 'bonnie_tyler-total_eclipse_of_the_heart.mid')
        output_path = os.path.join('output', 'new_teofth.mid')

        midi = Midi(data_path)
        midi.write(output_path)

        # files should be exactly the same
        f1 = BitArray(open(data_path)).hex
        f2 = BitArray(open(output_path)).hex

        for i, nib in enumerate(f1):
            self.assertEqual(nib, f2[i], msg="For nibble position %d, original data has %s and output data has %s" % (i, nib, f2[i]))

        new_midi = Midi(os.path.join('output', 'new_teofth.mid'))

    def tearDown(self):
        pass