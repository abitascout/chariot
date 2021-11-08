import sys

if(len(sys.argv) != 2):
  print("This program takes one variable: the name of the key file. It also takes an input using <, the file to be deciphered.")
  sys.exit()


#Open and assign contents of files to variables
message = bytearray(sys.stdin.buffer.read())
f = open(sys.argv[1], 'r')
key = bytearray(f.buffer.read())

#Xor each byte and append to output array
output = bytearray()
for i in range(len(message)):
  output.append(message[i] ^ key[i%len(key)])

#Write results
sys.stdout.buffer.write(output)