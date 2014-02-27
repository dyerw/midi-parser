import os
import random
import sys

generate_randomly = True
if len(sys.argv) == 3:
    sound1 = sys.argv[1]
    sound2 = sys.argv[2]
    generate_randomly = False

x = open(os.path.join('test_midis', 'pokemon-center.mid')).read()

hex_list = [val.encode('hex') for val in x]

if generate_randomly:
    sound1 = hex(random.choice(range(127)))[2:]
    sound2 = hex(random.choice(range(127)))[2:]

if len(sound1) == 1:
    sound1 = "0" + sound1
if len(sound2) == 1:
    sound2 = "0" + sound2

print sound1
print sound2

hex_list[24] = sound1
hex_list[27] = sound2

output = reduce((lambda a, b: a + b), [val.decode('hex') for val in hex_list])

open('output.mid', 'w').write(output)