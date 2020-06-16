#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *
# sys.path.append("./examples")

# from examples.print8 import *

# print8 = [
#     # From print8.ls8
#     0b10000010,  # LDI R0,8
#     0b00000000,  # address 0
#     0b00001000,  # store value 8
#     0b01000111,  # PRN R0 (i.e. print 8)
#     0b00000000,  # ??
#     0b00000001,  # HLT
# ]

# mult = [
#     0b10000010,  # LDI R0,8
#     0b00000000,  # @ reg[0]
#     0b00001000,  # store 8
#     0b10000010,  # LDI R1,9
#     0b00000001,  # @reg[1]
#     0b00001001,  # store 9
#     0b10100010,  # MUL R0,R1
#     0b00000000,  # get reg[0] = 8
#     0b00000001,  # get reg[1] = 6
#     0b01000111,  # PRN R0
#     0b00000000,  # call reg[0]
#     0b00000001,  # HLT
# ]

program = []

file_name = sys.argv[1]

with open(file_name) as f:
    lines = f.readlines()
    for line in lines:
        if line[0]!= '#':
            num = int(line[0:8], 2)
            program.append(num)
        print(program)

cpu = CPU()

cpu.load(program)
cpu.run()
