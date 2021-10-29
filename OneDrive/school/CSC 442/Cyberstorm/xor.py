import sys

#Open and assign contents of files to variables
message = bytearray(sys.stdin.buffer.read())
f = open('key', 'r')
key = bytearray(f.buffer.read())

#Xor each byte and append to output array
output = bytearray()
for i in range(len(message)):
  output.append(message[i] ^ key[i])

#Write results
sys.stdout.buffer.write(output)

"""
Questions: Consider an application of this program where the key is NOT the same size as the message (what would you do?)

Response: If the key was longer than the message, I would simply have it run as normal, as the loop stops at the size of the message. If the message were longer, however, when using the iterator to scan values from key, I would mod it by the length of key so that it could wrap back to the start of the bytearray.
"""