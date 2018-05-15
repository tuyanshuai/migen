from migen import *

from migen.fhdl import verilog
from migen.build.platforms import nexys4ddr
plat = nexys4ddr.Platform()

class Blinky(Module):
    def __init__(self):
        self.counter = Signal(max=1024)
        self.led =  Signal()
        
        self.comb += self.led.eq(self.counter[9])
        self.sync += self.counter.eq(self.counter + 1)
    
dut = Blinky()

print(verilog.convert(dut))

plat.build(dut)
