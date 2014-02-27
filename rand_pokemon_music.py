import os
import random

x = open(os.path.join('test_midis', 'pokemon-center.mid')).read()

hex_list = [val.encode('hex') for val in x]

sound1 = hex(random.choice(range(127)))[2:]
sound2 = hex(random.choice(range(127)))[2:]
print sound1
print sound2

hex_list[24] = sound1
hex_list[27] = sound2

output = reduce((lambda a, b: a + b), [val.decode('hex') for val in hex_list])

open('output.mid', 'w').write(output)