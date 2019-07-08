#!/usr/bin/env python3

import getopt
import mdtraj as md
import sys
import numpy as np


def usage():
    print("usage: ",sys.argv[0]," -o out.txt -t top.pdb traj.xtc")

try:
    opts, args = getopt.getopt(sys.argv[1:], 'o:t:')
except getopt.GetoptError as err:
    usage()
    sys.exit(1)

out=None
top=None

for o,a in opts:
    if o == '-o':
        out = a
    elif o == '-t': 
        top = a
    else:
        usage()
        sys.exit(1)

if not out or not top or not args:
    usage()
    sys.exit(1)
    

# XXX: ohavne pomale, cca. 100ms na ~4000 atomu v jednom pdb
# tr = md.load(sys.argv[1:])

tr = md.load(args[0],top=top)

idx=tr.top.select("protein and element != H")
tr.atom_slice(idx,inplace=True)

xyz = np.reshape(tr.xyz,(tr.xyz.shape[0],tr.xyz.shape[1]*3))
xyz_avg = np.average(xyz,axis=0)
xyz -= xyz_avg

cor = np.matmul(np.transpose(xyz),xyz)
cor /= xyz.shape[0]

#print("xyz: ",xyz.shape)
#print("cor: ",cor.shape)

eig = np.sort(np.linalg.eigvalsh(cor))

sum = np.sum(eig)
eig /= sum

np.savetxt(out,eig)
