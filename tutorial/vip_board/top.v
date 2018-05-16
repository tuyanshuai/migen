/* Machine-generated using Migen */
module top(
	output led595_clk,
	output led595_dout,
	output led595_latch,
	input clk
);

reg [9:0] cnt0 = 10'd0;
wire [7:0] binval;
reg [5:0] cnt1 = 6'd0;
wire dout;
reg latch = 1'd0;
wire ledclk;
reg [7:0] btmp = 8'd0;
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

assign binval = 8'd255;
assign led595_clk = ledclk;
assign led595_dout = 1'd1;
assign led595_latch = latch;
assign dout = btmp[7];
assign ledclk = cnt1[3];
assign sys_clk = clk;
assign por_clk = clk;
assign sys_rst = int_rst;

always @(posedge por_clk) begin
	int_rst <= 1'd0;
end

always @(posedge sys_clk) begin
	cnt0 <= (cnt0 + 1'd1);
	cnt1 <= (cnt1 + 1'd1);
	if ((cnt1 == 6'd63)) begin
		latch <= 1'd1;
		btmp <= binval;
	end else begin
		latch <= 1'd0;
		btmp <= (btmp <<< 1'd1);
	end
	if (sys_rst) begin
		cnt0 <= 10'd0;
		cnt1 <= 6'd0;
		latch <= 1'd0;
		btmp <= 8'd0;
	end
end

endmodule
