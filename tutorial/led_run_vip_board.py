#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 02:35:14 2018
led liushuideng 
@author: tys
"""


from migen import *
from migen.build.platforms import vip_board
import migen.fhdl.verilog as verilog
from showled import * 
 


class LEDTop(Module):
    def __init__(self, platform):
        ledclk = platform.request("led595_clk")
        leddout = platform.request("led595_dout") 
        ledlatch = platform.request("led595_latch")  

        
        cnt = Signal(10)
        binval =Signal(8) 
        
        m2 = showled(binval)      
        


        self.submodules += m2
        
        self.comb += binval.eq(0b11111111);
        self.comb += ledclk.eq(m2.ledclk);
        self.comb += leddout.eq(True);# m2.dout
        self.comb += ledlatch.eq(m2.latch);
        
        
        self.sync += cnt.eq(cnt+1)



platform = vip_board.Platform()


dut = LEDTop(platform)
 
#print(verilog.convert(dut))

platform.build(dut,build_dir="vip_board")

platform.create_programmer().load_bitstream("vip_board/top.sof")

