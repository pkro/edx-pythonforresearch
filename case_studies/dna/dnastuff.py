# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from dna_translate import translate, read_seq

seq = read_seq('dna.txt')
prt = read_seq('protein.txt')

print(translate(seq[20:938]) == prt)

