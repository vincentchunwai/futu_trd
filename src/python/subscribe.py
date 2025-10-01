import time
from futu import *
class OrderBook(OrderBookHandlerBase):
    def on_recv_rsp(self, rsp_pb):
        ret_code, data = super(OrderBook,self).on_recv_rsp(rsp_pb)
        if ret_code != RET_OK:
            print("OrderBookTest: error, msg: %s"% data)
            return RET_ERROR, data
        print("OrderBookTest ", data) # OrderBookTest's own processing logic
        return RET_OK, data
    

quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
handler = OrderBook()
quote_ctx.set_handler(handler) # Set real-time swing callback
quote_ctx.subscribe(['US.CRWV'], [SubType.ORDER_BOOK]) # Subscribe to the order type, OpenD starts to receive continuous push from the server
time.sleep(15) # Set the script to receive OpenD push duration to 15 seconds
quote_ctx.close()