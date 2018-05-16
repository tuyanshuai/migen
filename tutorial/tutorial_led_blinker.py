#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 09:25:07 2018

@author: tys
"""

from migen.fhdl import * 
from migen.sim  import *
import os

class Blinker(Module):
    def __init__(self, led, maxperiod):
        counter = Signal(max =maxperiod +1)
        period  = Signal(max =maxperiod +1)
        self.comb += period.eq(maxperiod)
        self.sync +=  If(counter ==0,
                         led.eq(~led),
                         counter.eq(period)
                       ).Else(
                               counter.eq(counter-1)
                       )


led =Signal()
my_blk = Blinker(led, 30000000)
print(verilog.convert(my_blk, ios={led}) )


