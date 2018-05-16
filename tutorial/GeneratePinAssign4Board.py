#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 17:47:49 2018

@author: tys
"""
tclfilestring ="""set_location_assignment PIN_89 -to clk
	set_location_assignment PIN_23 -to rst_n
	set_location_assignment PIN_32 -to led595_clk
	set_location_assignment PIN_34 -to led595_dout
	set_location_assignment PIN_33 -to led595_latch
	set_location_assignment PIN_24 -to key_data[1]
	set_location_assignment PIN_25 -to key_data[0]
	set_location_assignment PIN_137 -to lcd_dclk	
	set_location_assignment PIN_1   -to lcd_blank
	set_location_assignment PIN_136 -to lcd_hs
	set_location_assignment PIN_135 -to lcd_vs
	set_location_assignment PIN_34 -to lcd_red[0]
	set_location_assignment PIN_33 -to lcd_red[1]
	set_location_assignment PIN_32 -to lcd_red[2]
	set_location_assignment PIN_31 -to lcd_red[3]
	set_location_assignment PIN_30 -to lcd_red[4]
	set_location_assignment PIN_28 -to lcd_green[0]
	set_location_assignment PIN_11 -to lcd_green[1]
	set_location_assignment PIN_10 -to lcd_green[2]
	set_location_assignment PIN_7  -to lcd_green[3]
	set_location_assignment PIN_3  -to lcd_green[4]
	set_location_assignment PIN_2  -to lcd_green[5]
	set_location_assignment PIN_144 -to lcd_blue[0]
	set_location_assignment PIN_143 -to lcd_blue[1]
	set_location_assignment PIN_142 -to lcd_blue[2]
	set_location_assignment PIN_141 -to lcd_blue[3]
	set_location_assignment PIN_138 -to lcd_blue[4]	
	set_location_assignment PIN_51 -to sdram_clk
	set_location_assignment PIN_50 -to sdram_cke
	set_location_assignment PIN_64 -to sdram_cs_n
	set_location_assignment PIN_67 -to sdram_we_n
	set_location_assignment PIN_66 -to sdram_cas_n
	set_location_assignment PIN_65 -to sdram_ras_n
	set_location_assignment PIN_60 -to sdram_ba[0]
	set_location_assignment PIN_59 -to sdram_ba[1]
	set_location_assignment PIN_55 -to sdram_addr[0]
	set_location_assignment PIN_54 -to sdram_addr[1]
	set_location_assignment PIN_53 -to sdram_addr[2]
	set_location_assignment PIN_52 -to sdram_addr[3]
	set_location_assignment PIN_38 -to sdram_addr[4]
	set_location_assignment PIN_39 -to sdram_addr[5]
	set_location_assignment PIN_42 -to sdram_addr[6]
	set_location_assignment PIN_43 -to sdram_addr[7]
	set_location_assignment PIN_44 -to sdram_addr[8]
	set_location_assignment PIN_46 -to sdram_addr[9]
	set_location_assignment PIN_58 -to sdram_addr[10]
	set_location_assignment PIN_49 -to sdram_addr[11]
	set_location_assignment PIN_75 -to sdram_data[0]
	set_location_assignment PIN_74 -to sdram_data[1]
	set_location_assignment PIN_73 -to sdram_data[2]
	set_location_assignment PIN_72 -to sdram_data[3]
	set_location_assignment PIN_71 -to sdram_data[4]
	set_location_assignment PIN_70 -to sdram_data[5]
	set_location_assignment PIN_69 -to sdram_data[6]
	set_location_assignment PIN_68 -to sdram_data[7]
	set_location_assignment PIN_76 -to sdram_data[8]
	set_location_assignment PIN_77 -to sdram_data[9]
	set_location_assignment PIN_80 -to sdram_data[10]
	set_location_assignment PIN_83 -to sdram_data[11]
	set_location_assignment PIN_84 -to sdram_data[12]
	set_location_assignment PIN_85 -to sdram_data[13]
	set_location_assignment PIN_86 -to sdram_data[14]
	set_location_assignment PIN_87 -to sdram_data[15]
	set_location_assignment PIN_88 -to cmos_pclk
	set_location_assignment PIN_115 -to cmos_sclk
	set_location_assignment PIN_114 -to cmos_sdat
	set_location_assignment PIN_120 -to cmos_vsync
	set_location_assignment PIN_119 -to cmos_href
	set_location_assignment PIN_121 -to cmos_xclk
	set_location_assignment PIN_124 -to cmos_data[7]
	set_location_assignment PIN_125 -to cmos_data[6]
	set_location_assignment PIN_126 -to cmos_data[5]
	set_location_assignment PIN_127 -to cmos_data[4]
	set_location_assignment PIN_128 -to cmos_data[3]
	set_location_assignment PIN_129 -to cmos_data[2]
	set_location_assignment PIN_132 -to cmos_data[1]
	set_location_assignment PIN_133 -to cmos_data[0]
	set_location_assignment PIN_113 -to USB_IFCLK
	set_location_assignment PIN_112 -to USB_WR
	set_location_assignment PIN_91 -to USB_Trigger
	set_location_assignment PIN_98  -to USB_Data[0]
	set_location_assignment PIN_99  -to USB_Data[1]
	set_location_assignment PIN_100 -to USB_Data[2]
	set_location_assignment PIN_101 -to USB_Data[3]
	set_location_assignment PIN_103 -to USB_Data[4]
	set_location_assignment PIN_104 -to USB_Data[5]
	set_location_assignment PIN_105 -to USB_Data[6]
	set_location_assignment PIN_106 -to USB_Data[7]
	set_location_assignment PIN_111  -to USB_PD3
	set_location_assignment PIN_110  -to USB_PD4
	set_location_assignment PIN_91 -to USB_PD5
	set_location_assignment PIN_90 -to USB_PD6
    """
    
pstr =tclfilestring
for i in range(92):
    ind = pstr.find("PIN_")
    ind2 = pstr.find("-to")
    ind3 = pstr.find('\n');
    pin =  pstr[ind+4:ind2-1]    
    port =  pstr[ind2+4:ind3]
    
    sl = port.find('[')
    sr = port.find(']')
    id ='0'
    if sl != -1:
        id = port[sl+1:sr]
        port = port[0:sl]
        
            
    print('("' +port + '", ' + id + ', Pins("' +pin+'"), IOStandard("3.3-V LVTTL")),') 
    
    pstr=pstr[ind3+1:]
    