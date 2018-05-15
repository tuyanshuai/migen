# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from migen import *
from migen.fhdl import verilog


class Sub(Module):
    def __init__(self, x, y, sub, borrow):
      
         
        self.sync += sub.eq(x - y)      
        
        
        self.sync += If(x>=y,
                        borrow.eq(0)
                        ).Else(
                        borrow.eq(1) )


Width = 10
x = Signal(Width)
y = Signal(Width)
sub = Signal(Width)
borrow = Signal()

if __name__ == "__main__":
    print(verilog.convert(Sub(x,y, sub,borrow), ios={x,y,sub,borrow}))