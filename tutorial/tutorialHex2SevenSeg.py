#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 16:45:22 2018

@author: tys
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

bcd27seg
"""

from migen import *
from migen.fhdl import verilog


class Hex2SevenSeg(Module):
    def __init__(self):
        
        self.bcd = value = Signal(4)
        
        self.abcdefg = abcdefg = Signal(7)
        
        cases = {
          0x0: abcdefg.eq(0b0111111),
          0x1: abcdefg.eq(0b0000110),
          0x2: abcdefg.eq(0b1011011),
          0x3: abcdefg.eq(0b1001111),
          0x4: abcdefg.eq(0b1100110),
          0x5: abcdefg.eq(0b1101101),
          0x6: abcdefg.eq(0b1111101),
          0x7: abcdefg.eq(0b0000111),
          0x8: abcdefg.eq(0b1111111),
          0x9: abcdefg.eq(0b1101111),
          0xa: abcdefg.eq(0b1110111),
          0xb: abcdefg.eq(0b1111100),
          0xc: abcdefg.eq(0b0111001),
          0xd: abcdefg.eq(0b1011110),
          0xe: abcdefg.eq(0b1111001),
          0xf: abcdefg.eq(0b1110001),
        }

        # combinatorial assignement
        self.comb += Case(value, cases)
        
             
      
if __name__ == "__main__":
    dut = Hex2SevenSeg()
    print(verilog.convert(dut, ios ={ dut.bcd, dut.abcdefg}))