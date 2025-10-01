from futu import *
import backtest # pyright: ignore[reportMissingImports]

def get_stock_data(code):
    backtest.backtest()
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    result = quote_ctx.get_market_snapshot(code)

    if result[0] == RET_OK:
        data = result[1]
        
        #print("=== Available Columns ===")
        #print(data.columns.tolist())
        #print()

        print(data["code"].iloc[0])
        print(data["name"].iloc[0])
        print(f"Last price: {data["last_price"].iloc[0]}")
        print(f"Volume: {data['volume'].iloc[0]}")
        #print(data["open_price"])
        #print(data["high_price"])

    quote_ctx.close()

def buy_stock(price, qty, code):
    pwd_unlock = input("Enter trading password to unlock: ")
    if not pwd_unlock:
        print("No password entered, cannot proceed with buying.")
        return
    trade_ctx = OpenSecTradeContext(filter_trdmarket=TrdMarket.US, host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
    ret, data = trade_ctx.unlock_trade(pwd_unlock)
    if ret == RET_OK:
        ret, data = trade_ctx.place_order(price=price, qty=qty, code=code, trd_side=TrdSide.BUY, order_type=OrderType.NORMAL)
        if ret == RET_OK:
            print("Order placed successfully, order ID:", data['order_id'][0])
        else:
            print("Failed to place order:", data)
    else:
        print("Failed to unlock trade:", data)
    trade_ctx.close()



if __name__ == "__main__":
    get_stock_data('US.RZLV')
    #buy_stock(5.0, 1, 'US.RZLV')