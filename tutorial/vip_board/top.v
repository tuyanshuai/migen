/* Machine-generated using Migen */
module top(
	output led595_clk,
	output reg led595_dout,
	output led595_latch,
	input clk
);

reg [24:0] counter = 25'd0;
reg [7:0] Number = 8'd0;
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

assign led595_clk = counter[22];
assign led595_latch = counter[24];
assign sys_clk = clk;
assign por_clk = clk;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	counter <= (counter + 1'd1);
	Number <= (Number + 1'd1);
	led595_dout <= counter[23];
	if (sys_rst) begin
		led595_dout <= 1'd0;
		counter <= 25'd0;
		Number <= 8'd0;
	end
end

endmodule
