# This file is Copyright (c) 2013 Florent Kermarrec <florent@enjoy-digital.fr>
# License: BSD

from migen.build.generic_platform import *
from migen.build.altera import AlteraPlatform
from migen.build.altera.programmer import USBBlaster


_io = [
    ("clk", 0, Pins("89"), IOStandard("3.3-V LVTTL")),
    ("rst_n", 0, Pins("23"), IOStandard("3.3-V LVTTL")),
    ("led595_clk", 0, Pins("32"), IOStandard("3.3-V LVTTL")),
    ("led595_dout", 0, Pins("34"), IOStandard("3.3-V LVTTL")),
    ("led595_latch", 0, Pins("33"), IOStandard("3.3-V LVTTL")),
    ("key_data", 1, Pins("24"), IOStandard("3.3-V LVTTL")),
    ("key_data", 0, Pins("25"), IOStandard("3.3-V LVTTL")),
    ("lcd_dclk", 0, Pins("137"), IOStandard("3.3-V LVTTL")),
    ("lcd_blank", 0, Pins("1  "), IOStandard("3.3-V LVTTL")),
    ("lcd_hs", 0, Pins("136"), IOStandard("3.3-V LVTTL")),
    ("lcd_vs", 0, Pins("135"), IOStandard("3.3-V LVTTL")),
    ("lcd_red", 0, Pins("34"), IOStandard("3.3-V LVTTL")),
    ("lcd_red", 1, Pins("33"), IOStandard("3.3-V LVTTL")),
    ("lcd_red", 2, Pins("32"), IOStandard("3.3-V LVTTL")),
    ("lcd_red", 3, Pins("31"), IOStandard("3.3-V LVTTL")),
    ("lcd_red", 4, Pins("30"), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 0, Pins("28"), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 1, Pins("11"), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 2, Pins("10"), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 3, Pins("7 "), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 4, Pins("3 "), IOStandard("3.3-V LVTTL")),
    ("lcd_green", 5, Pins("2 "), IOStandard("3.3-V LVTTL")),
    ("lcd_blue", 0, Pins("144"), IOStandard("3.3-V LVTTL")),
    ("lcd_blue", 1, Pins("143"), IOStandard("3.3-V LVTTL")),
    ("lcd_blue", 2, Pins("142"), IOStandard("3.3-V LVTTL")),
    ("lcd_blue", 3, Pins("141"), IOStandard("3.3-V LVTTL")),
    ("lcd_blue", 4, Pins("138"), IOStandard("3.3-V LVTTL")),
    ("sdram_clk", 0, Pins("51"), IOStandard("3.3-V LVTTL")),
    ("sdram_cke", 0, Pins("50"), IOStandard("3.3-V LVTTL")),
    ("sdram_cs_n", 0, Pins("64"), IOStandard("3.3-V LVTTL")),
    ("sdram_we_n", 0, Pins("67"), IOStandard("3.3-V LVTTL")),
    ("sdram_cas_n", 0, Pins("66"), IOStandard("3.3-V LVTTL")),
    ("sdram_ras_n", 0, Pins("65"), IOStandard("3.3-V LVTTL")),
    ("sdram_ba", 0, Pins("60"), IOStandard("3.3-V LVTTL")),
    ("sdram_ba", 1, Pins("59"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 0, Pins("55"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 1, Pins("54"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 2, Pins("53"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 3, Pins("52"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 4, Pins("38"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 5, Pins("39"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 6, Pins("42"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 7, Pins("43"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 8, Pins("44"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 9, Pins("46"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 10, Pins("58"), IOStandard("3.3-V LVTTL")),
    ("sdram_addr", 11, Pins("49"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 0, Pins("75"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 1, Pins("74"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 2, Pins("73"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 3, Pins("72"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 4, Pins("71"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 5, Pins("70"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 6, Pins("69"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 7, Pins("68"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 8, Pins("76"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 9, Pins("77"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 10, Pins("80"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 11, Pins("83"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 12, Pins("84"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 13, Pins("85"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 14, Pins("86"), IOStandard("3.3-V LVTTL")),
    ("sdram_data", 15, Pins("87"), IOStandard("3.3-V LVTTL")),
    ("cmos_pclk", 0, Pins("88"), IOStandard("3.3-V LVTTL")),
    ("cmos_sclk", 0, Pins("115"), IOStandard("3.3-V LVTTL")),
    ("cmos_sdat", 0, Pins("114"), IOStandard("3.3-V LVTTL")),
    ("cmos_vsync", 0, Pins("120"), IOStandard("3.3-V LVTTL")),
    ("cmos_href", 0, Pins("119"), IOStandard("3.3-V LVTTL")),
    ("cmos_xclk", 0, Pins("121"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 7, Pins("124"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 6, Pins("125"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 5, Pins("126"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 4, Pins("127"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 3, Pins("128"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 2, Pins("129"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 1, Pins("132"), IOStandard("3.3-V LVTTL")),
    ("cmos_data", 0, Pins("133"), IOStandard("3.3-V LVTTL")),
    ("USB_IFCLK", 0, Pins("113"), IOStandard("3.3-V LVTTL")),
    ("USB_WR", 0, Pins("112"), IOStandard("3.3-V LVTTL")),
    ("USB_Trigger", 0, Pins("91"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 0, Pins("98 "), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 1, Pins("99 "), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 2, Pins("100"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 3, Pins("101"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 4, Pins("103"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 5, Pins("104"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 6, Pins("105"), IOStandard("3.3-V LVTTL")),
    ("USB_Data", 7, Pins("106"), IOStandard("3.3-V LVTTL")),
    ("USB_PD3", 0, Pins("111 "), IOStandard("3.3-V LVTTL")),
    ("USB_PD4", 0, Pins("110 "), IOStandard("3.3-V LVTTL")),
    ("USB_PD5", 0, Pins("91"), IOStandard("3.3-V LVTTL")),
    ("USB_PD6", 0, Pins("90"), IOStandard("3.3-V LVTTL")),
]


class Platform(AlteraPlatform):
    default_clk_name = "clk"
    default_clk_period = 41.666666666666664

    def __init__(self):
        AlteraPlatform.__init__(self, "EP4CE10E22C8N", _io)

    def create_programmer(self):
        return USBBlaster()

    def print_io(self):
        import pprint
        pprint.pprint(_io)