from bitstring import BitStream, Bits


def read_variable_byte_data(bit_stream, data_bits=Bits('')):
    continuation_bit = bit_stream.read('bits:1')
    data_bits += bit_stream.read('bits:7')

    if continuation_bit:
        return read_variable_byte_data(bit_stream, data_bits)
    else:
        while len(data_bits) % 8 != 0:
            data_bits = BitStream('0b0') + data_bits
        return data_bits
