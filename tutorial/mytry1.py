#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 03:01:44 2018

@author: tys
"""

from migen import *

from migen.build.platforms import nexys4ddr




class MyLed(Module):
    def __init__(self, platform):
        self.led = platform.request("user_led")      
        self.counter = Signal(25)        
        self.comb += self.led.eq(self.counter[24]);
        self.sync += self.counter.eq(self.counter+1)
        
 
platform = nexys4ddr.Platform()
dut = MyLed(platform)


print(fhdl.verilog.convert(dut))

platform.build(dut, build_dir = "build_mytry1")

 
