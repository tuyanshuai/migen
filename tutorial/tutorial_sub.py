# -*- coding: utf-8 -*-
"""
Spyder Editor

substractor
"""

from migen import *
from migen.fhdl import verilog


class Sub(Module):
    def __init__(self, width):
      
        self.a = a = Signal(width)
        self.b = b = Signal(width)
        self.sub = sub = Signal(width) 
        
        self.borrow = borrow = Signal()
        self.sync += sub.eq(a - b)
        self.sync += If(a>=b, borrow.eq(0)).Else(borrow.eq(1))        
      
if __name__ == "__main__":
    dut = Sub(10)
    print(verilog.convert(dut, ios ={ dut.a, dut.b, dut.sub, dut.borrow}))