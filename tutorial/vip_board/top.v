/* Machine-generated using Migen */
module top(
	output led595_clk,
	output reg led595_dout,
	output led595_latch,
	output cmos_data,
	output cmos_data_1,
	output cmos_data_2,
	output cmos_data_3,
	output cmos_data_4,
	output cmos_data_5,
	output cmos_data_6,
	output cmos_data_7,
	input clk50
);

reg [24:0] counter = 25'd0;
wire sys_clk;
wire sys_rst;
wire por_clk;
reg int_rst = 1'd1;


// Adding a dummy event (using a dummy signal 'dummy_s') to get the simulator
// to run the combinatorial process once at the beginning.
// synthesis translate_off
reg dummy_s;
initial dummy_s <= 1'd0;
// synthesis translate_on

assign cmos_data = 1'd0;
assign cmos_data_1 = 1'd0;
assign cmos_data_2 = 1'd0;
assign cmos_data_3 = 1'd0;
assign cmos_data_4 = 1'd0;
assign cmos_data_5 = 1'd0;
assign cmos_data_6 = 1'd0;
assign cmos_data_7 = 1'd0;
assign led595_clk = counter[22];
assign led595_latch = counter[24];
assign sys_clk = clk50;
assign por_clk = clk50;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	counter <= (counter + 1'd1);
	led595_dout <= counter[23];
	if (sys_rst) begin
		led595_dout <= 1'd0;
		counter <= 25'd0;
	end
end

endmodule
