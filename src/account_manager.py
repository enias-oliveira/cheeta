from .user import User
from .market_hypothesis import MarketHypothesis


class AccountManager:
    def __init__(self, users: list[User]):
        self.users = users

    def process_market_hypothesis(hypothesis: MarketHypothesis):
        ...
