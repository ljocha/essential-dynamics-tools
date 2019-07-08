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

one = np.flip(one[-num:])
two = np.flip(two[-num:])

plt.figure(figsize=((10,15)))
plt.subplot(311)
plt.plot(range(num),one)
plt.plot(range(num),two)
plt.grid()
plt.legend(args)
plt.ylabel("Eigenvalues (linear)")

plt.subplot(312)
plt.plot(range(num),np.log(one))
plt.plot(range(num),np.log(two))
plt.grid()
plt.legend(args)
plt.ylabel("Eigenvalues (log)")


plt.subplot(313)
plt.plot(range(num),np.cumsum(one))
plt.plot(range(num),np.cumsum(two))
plt.grid()
plt.ylabel("Cummulative")
plt.legend(args)
plt.show()

