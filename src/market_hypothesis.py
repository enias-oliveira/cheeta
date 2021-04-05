class MarketHypothesis:
    @staticmethod
    def _calculate_risk_level(volume: float):
        from .trade import Trade

        if volume > Trade.TRADE_LEVELS_VOLUMES[1]:
            return 1
        elif volume > Trade.TRADE_LEVELS_VOLUMES[2]:
            return 2
        elif volume > Trade.TRADE_LEVELS_VOLUMES[3]:
            return 3
        else:
            return None

    def __init__(
        self,
        market: str,
        trading_pair: str,
        side: str,
        price: float,
        exchange: str,
        volume: float,
        hypothesis_id: str,
        *args,
        **kwargs,
    ):
        self.market = market
        self.trading_pair = trading_pair
        self.side = side
        self.price = float(price)
        self.exchange = exchange
        self.volume = float(volume)
        self.hypothesis_id = hypothesis_id
        self.risk_level = MarketHypothesis._calculate_risk_level(volume)

    def _set_risk_level(self, level: int):
        self.risk_level = level

    def _get_risk_level(self):
        return self.risk_level

    def __str__(self):
        return f"Hypothesis: {self.side} - {self.trading_pair}/{self.market}\nExchange: {self.exchange}\nPrice: {self.price}"
