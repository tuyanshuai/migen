#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 20:06:42 2018

@author: tys
"""

from migen import *
from migen.fhdl import verilog


class clockgen(Module):
    """
    a frequency divider
    
    """
    def __init__(self, fre_in = 24, fre_out = 1):
        
            
      
        halfcnt = int( fre_in/fre_out/2);
        
        #print(halfcnt)
        
        
        self.half_period_cnt = Signal(max = halfcnt)
        self.out_clk = Signal(name="led_clk")
        
        # self.comb += [self.half_period_cnt[0:15].eq(self.divider[1:])]
        
       
               
        self.sync += [
            If(self.half_period_cnt == halfcnt-1,
               self.out_clk.eq(~self.out_clk), 
               self.half_period_cnt.eq(0)
              ).Else(
                self.half_period_cnt.eq(self.half_period_cnt+1))]

if __name__ == "__main__":
    m = clockgen(fre_out =2)
    print(verilog.convert(m, ios={m.out_clk}))