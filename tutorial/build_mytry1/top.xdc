 ## user_led:0
set_property LOC H17 [get_ports user_led]
set_property IOSTANDARD LVCMOS33 [get_ports user_led]
 ## clk100:0
set_property LOC E3 [get_ports clk100]
set_property IOSTANDARD LVCMOS33 [get_ports clk100]

set_property INTERNAL_VREF 0.750 [get_iobanks 34]

create_clock -name clk100 -period 10.0 [get_nets clk100]

set_false_path -quiet -to [get_nets -filter {mr_ff == TRUE}]

set_false_path -quiet -to [get_pins -filter {REF_PIN_NAME == PRE} -of [get_cells -filter {ars_ff1 == TRUE || ars_ff2 == TRUE}]]

set_max_delay 2 -quiet -from [get_pins -filter {REF_PIN_NAME == Q} -of [get_cells -filter {ars_ff1 == TRUE}]] -to [get_pins -filter {REF_PIN_NAME == D} -of [get_cells -filter {ars_ff2 == TRUE}]]