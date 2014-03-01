import os
import random


#open the midi file
x = open(os.path.join('../test_midis', 'pokemon-center.mid')).read()

#encode each ascii value in midi file to its hex equivilent
hex_list = [val.encode('hex') for val in x]

#if user did not specify instruments to be assigned, assign a random one to each
#with any given sound bank there are 0-127 options for instruments

found_first = False
found_second = False

#checks the list for the first note played by each instrument, saving the values to 'root' and 'third' respectively
for i in range(0, len(hex_list)):
    if not found_first:
        if hex_list[i] == '90':
            root = hex_list[i + 1]
            found = True
    if not found_second:
        if hex_list[i] == '91':
            third = hex_list[i+1]
            found = True

#prints the instrument choices to the user
print root
print third
print "ended"

#I want to create a dictionary who's keys are 0-127 and who's values range chromatically starting at C0
#That way based on the first noted played (could be found by knowing looking at the first notes played with delay 00)
#we could actually get a the note names in the first chord. taking that forward, it wouldn't be hard to actually get
# the chord progression
#from the midi file

#we must now decode our hex back into ascii so it can be written to the .mid properly
output = reduce((lambda a, b: a + b), [val.decode('hex') for val in hex_list])

#open the file location 'output.mid' and write the ascii back to the file
open('../output.mid', 'w').write(output)
