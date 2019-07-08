#!/usr/bin/env python3

import getopt
import sys
import numpy as np
import matplotlib.pyplot as plt

def usage():
    print("usage: ",sys.argv[0]," [-n num] one.txt two.txt")

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:')
except getopt.GetoptError as err:
    usage()
    sys.exit(1)

num=None

for o,a in opts:
    if o == '-n':
        num = int(a)
    else:
        usage()
        sys.exit(1)

if len(args) != 2:
    usage()
    sys.exit(1)


one = np.loadtxt(args[0])
two = np.loadtxt(args[1])

if not num:
    num = len(one)

cone = np.cumsum(np.flip(one))
ctwo = np.cumsum(np.flip(two))

plt.figure(figsize=((10,5)))
plt.subplot(211)
plt.plot(range(num),np.flip(one[-num:]))
plt.plot(range(num),np.flip(two[-num:]))
plt.grid()
plt.legend(args)
plt.ylabel("Eigenvalues")
plt.subplot(212)
plt.plot(range(num),cone[:num])
plt.plot(range(num),ctwo[:num])
plt.grid()
plt.ylabel("Cummulative")
plt.legend(args)
plt.show()

