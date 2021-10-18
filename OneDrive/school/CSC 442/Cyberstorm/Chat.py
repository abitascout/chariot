###############################################################################
# Names: Abdullah Alshamdayn, Joy Brown, Caitlin Burke, Samantha Gnagey
#        Robert Morton, Kyler Parker
# Group: Chariot
# Date: 10/14/2021
# Assignment: Program 4: Chat (Timing) Covert Channel
###############################################################################

# Import statements
from time import time
import socket
from sys import stdout


# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = '138.47.99.64'
#port = 1337
port = 12000

# using the time 0 or 1 for the covert message
tt1 = 0.025
tt2 = .1
avg = (tt2 + tt1) / 2

# We utilized our function from the previous assignments with some small enhancements
def ConvertToA(i, n, s):
    final = ""
    for index in range(0, n-(s-1), s):
        num = int(i[index:index + s], 2)
        if num == 8:
            final = final[:-1]
        else:
            final += chr(num)
    print("Covert message: {}".format(final).split("EOF")[0])
    return

# a function to receive data until EOF
def gCov(s):
    BStr = ""
    data = s.recv(4096).decode()
    while data.rstrip("\n") != 'EOF':
        # output the data
        stdout.write(data)
        stdout.flush()
        # start the "timer", get more data, and end the "timer"
        t0 = time()
        data = s.recv(4096).decode()
        t1 = time()
        # calculate the time delta (and output if debugging)
        delta = round(t1 - t0, 3)
        if DEBUG:
            stdout.write(" {}\n".format(delta))
            stdout.flush()
            print("")
            print(delta)
        if delta <= avg:
            BStr += "0"
        else:
            BStr += "1"
    print("...\n[disconnect from the chat server]")
    s.close()

    if DEBUG:
        print(BStr)
    ConvertToA(BStr, len(BStr), 8)


if __name__ == '__main__':
    # create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    s.connect((ip, port))
    print("[connect to the chat server]\n...")
    gCov(s)
    # close the connection to the server
    s.close()
