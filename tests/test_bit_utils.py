import unittest
from bitstring import BitStream
from utils.bit_utils import read_variable_byte_data


class TestBitUtils(unittest.TestCase):
    def setUp(self):
        # This is 543 (base 10) represented over two bytes
        # The first bit is a continuation bit (1) and the
        # ninth bit is an end bit (0)
        self.variable_bytes = BitStream('0b1000010000011111')

    def test_read_variable_byte_data(self):

        data = read_variable_byte_data(self.variable_bytes)

        self.assertEqual(data.int, 543)

    def test_bit_stream_pointer_after_variable_bytes(self):
        """
        This tests that you can continue reading from where the pointer
        left off after read_variable_byte_data
        """

        var_bytes_plus_six = self.variable_bytes + BitStream('0b00000110')

        self.assertEqual(read_variable_byte_data(var_bytes_plus_six).int, 543)

        self.assertEqual(var_bytes_plus_six.read('bits:8').int, 6)

    def tearDown(self):
        pass