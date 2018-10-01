#!/usr/bin/env python3

from random import shuffle
from collections import OrderedDict 

groups_at_risc = [
    "D_L1",
    "D_L2"
]

groups_no_risc = [
    "C_L1",
    "C_L2"
]

lists_at_risc = [
    "bi",
    "uni"
]

lists_no_risc = [
    "bi",
    "uni"
]

shuffle(lists_at_risc)
shuffle(lists_no_risc)

at_risc = {
    groups_at_risc[0] : lists_at_risc[0],
    groups_at_risc[1] : lists_at_risc[1]
}

no_risc = {
    groups_no_risc[0] : lists_no_risc[0],
    groups_no_risc[1] : lists_no_risc[1]
}

for g, l in at_risc.items():
    print("group {} has list {}".format(g, l) )

for g, l in no_risc.items():
    print("group {} has list {}".format(g, l) )
