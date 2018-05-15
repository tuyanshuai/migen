#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 02:35:14 2018

@author: tys
"""


from migen import *
from migen.build.platforms import vip_board
from migen.fhdl.verilog import convert
 
class MyLedBlink(Module):
    def __init__(self, platform):
        

        self.ledclk =  platform.request("led595_clk")
        self.dout   =  platform.request("led595_dout") 
        self.latch  =  platform.request("led595_latch")  
         
        ### 
        
        counter = Signal(25) 
        clk = Signal();
        clk.eq(counter[14]); 
        
        Number = Signal(8);
        
        self.sync += counter.eq(counter + 1)
        self.sync += Number.eq(Number + 1)             
        self.comb += self.ledclk.eq(counter[22])        
        self.sync += self.dout.eq(counter[23]);        
        self.comb += self.latch.eq(counter[24]);
        
        
platform = vip_board.Platform()
dut = MyLedBlink(platform )

#print(convert(dut, ios={dut.ledclk, dut.dout, dut.latch}))
platform.build(dut,build_dir="vip_board")

platform.create_programmer().load_bitstream("vip_board/top.sof")
