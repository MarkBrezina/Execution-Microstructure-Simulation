def match_market_order(order_book, size, side):

    trades = []

    if side == "buy":
        book_side = sorted(order_book.asks.items())

    else:
        book_side = sorted(order_book.bids.items(), reverse=True)

    for price, liquidity in book_side:

        traded = min(size, liquidity)

        trades.append((price, traded))

        size -= traded

        if size == 0:
            break

    return trades
