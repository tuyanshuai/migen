#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 20:32:05 2018

@author: tys
"""
from migen import *
from migen.build.platforms import vip_board
import migen.fhdl.verilog as verilog

class showled(Module):
    def __init__(self, binval):
        
                     
        cnt = Signal(6)
        cnt_h = cnt[3:6]
        
        
        self.dout = Signal() 
        self.latch = Signal()
        self.ledclk = Signal()
        
        
        btmp = Signal(8)              
        
        self.comb += self.dout.eq(btmp[7])
        
        self.comb += self.ledclk.eq(cnt[3])
        
        
        

        
        
        self.sync  += cnt.eq(cnt+1)
        self.sync  += If(cnt == 2**6-1, 
                        self.latch.eq(True),
                        btmp.eq(binval)
                       ).Else(
                        self.latch.eq(False),
                        btmp.eq( btmp<< 1 )
                       )
        
        
if __name__ == "__main__":
    binval = Signal(8)
    s1 = showled(binval)
    
    print(verilog.convert(s1, ios={s1.dout,s1.latch}))
