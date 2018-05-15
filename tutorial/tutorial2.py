#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 01:53:17 2018

@author: tys
"""

from migen import *
from migen.build.platforms import nexys4ddr
from migen.fhdl.verilog import convert
 
class MyLedBlink(Module):
    def __init__(self, platform):
        self.led = led = platform.request("user_led")
        counter = Signal(25)
 
        self.sync += counter.eq(counter + 1)
        self.comb += led.eq(counter[24])
 
platform = nexys4ddr.Platform()
dut = MyLedBlink(platform)
platform.build(dut,build_dir="xilinx")
