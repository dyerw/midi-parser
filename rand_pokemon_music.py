import os
import random
import sys

#set generate randomly to true, unless user passes 3 arguments (the minimum for two one digit instrument choices)
generate_randomly = True

# if three args are passed, set the instrument values to the user's specifications
# set generate_randomly switch bool to false so our new values are not overwritten

if len(sys.argv) == 3:
    sound1 = sys.argv[1]
    sound2 = sys.argv[2]
    generate_randomly = False

#open the midi file
x = open(os.path.join('test_midis', 'pokemon-center.mid')).read()

#encode each ascii value in midi file to its hex equivilent
hex_list = [val.encode('hex') for val in x]

#if user did not specify instruments to be assigned, assign a random one to each
#with any given sound bank there are 0-127 options for instruments

if generate_randomly:
    sound1 = hex(random.choice(range(127)))[2:]
    sound2 = hex(random.choice(range(127)))[2:]

#each instrument in the file encoding must be a 1 word hex code
#this block fixes an issue where single digts were placed without a preceding zero
if len(sound1) == 1:
    sound1 = "0" + sound1
if len(sound2) == 1:
    sound2 = "0" + sound2

#prints the instrument choices to the user
print sound1
print sound2

#change the words at location 24 and 27 in midi file to the new hex word vals
#NOTE: this is currently file specific to pokemon-center.mid
hex_list[24] = sound1
hex_list[27] = sound2

#we must now decode our hex back into askii so it can be written to the .mid properly
output = reduce((lambda a, b: a + b), [val.decode('hex') for val in hex_list])

#open the file location 'output.mid' and write the ascii back to the file
open('output.mid', 'w').write(output)