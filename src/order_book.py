
class OrderBook:

    def __init__(self):
        self.bids = {}
        self.asks = {}

    def add_order(self, price, size, side):

        if side == "bid":
            self.bids.setdefault(price, 0)
            self.bids[price] += size

        else:
            self.asks.setdefault(price, 0)
            self.asks[price] += size
