import requests


class MarketHypothesisReceiver:
    MH_BASE_URL = "https://mininghamster.com/api/v2/"

    def __init__(self, mining_hamster=False, mining_hamster_key=""):
        self.mining_hamster_key = mining_hamster_key

    def _get_mining_hamster_signal(self):
        uri = f"{MarketHypothesisReceiver}{self.mining_hamster_key}"
        response = requests.get(uri)

        if response.ok:
            return response.json()[0]
        else:
            return None
