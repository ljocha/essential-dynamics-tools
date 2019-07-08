# essential-dynamics-tools
Simple tools to compute and compare essential dynamics of proteins

## mergepdb.sh

Get a bunch of PDB files, assuming they are aligned on each other, and merge them into a single XTC trajectory.

Files can be provided on command line or as a file listing them (to avoid "Argument list too long" bash complaints).

Usage:

```./mergepdb.sh -o outfile [-l list_of_files] [infiles ...]```

## calc_esd.py

Read a topology (PDB, GRO) and trajectory (XTC, TRR, ...) files, strip anything but protein heavy atoms, and calculate essential dynamics coordinates according to [https://doi.org/10.1002/prot.340170408](Amadei, A. et al, Essential dynamics of proteins, Proteins 17(4):412-24, 1993.)

Technically, eigenvalues of the correlation matrix of movements of all the heavy atoms
are computed. 

Output is a sorted numpy array dumped as text.

Usage:
```./calc_esd.py -o out.txt -t top.pdb traj.xtc"```


## draw_esd.py

Draw graphs of two sets of normalized eigenvalues computed by calc_esd.py. Number of largest eigenvalues to be considered can be secified (all by default).

Usage:
```./draw_esd.py  [-n num] one.txt two.txt```
