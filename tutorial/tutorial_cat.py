# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from migen import *
from migen.fhdl import verilog


class Example(Module):
    def __init__(self , a, b, s3, d):
      
        c = Signal(5)
      
        s1 = c[:3][:2]
        s2 = Cat(a, b)[:6]    
        self.comb += s3.eq(Cat(s1, s2)[-5:])
        self.comb += d.eq(Cat(d[::-1], Cat(s1[:1], s3[-4:])[:3]))

a = Signal(3)
b = Signal(4)
d = Signal(7)
s3 = Signal(10)
if __name__ == "__main__":
    print(verilog.convert(Example(a,b,s3,d)  ,  ios={a,b,d,s3}))