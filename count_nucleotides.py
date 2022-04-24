#!/usr/bin/env python3
seq = "ACTGCATTAGCAGTGCATGCTAGCTGTAGCATCGTCGTAGCACTAGCTACTAGCAATCTGAG"

d = {}

for nuc in seq:
    d[nuc] = d[nuc] + 1 if nuc in d else 1

print(d)
