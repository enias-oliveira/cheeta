import requests


class MiningHamsterSignalReceiver:
    BASE_URL = "https://mininghamster.com/api/v2/"

    def __init__(self, key):
        self.key = key
        self.last_buy_signal_id = ""
        # self.account_manager = account_manager

    def start_receiver(self):
        print("Listening to Mining Hamster")

        signal = self._get_signal()

        if signal["signal_id"] == self.last_buy_signal_id:
            return

        print("Signal Received:")

        # converted_buy_signal = MiningHamsterSignalReceiver._convert_signal_to_MH(signal)
        # buy_MH_from_signal = MarketHypothesis(converted_buy_signal)

        # account_manager.process_market_hypothesis(buy_MH_from_signal)

        # print(f"Processing:\n{buy_MH_from_signal}")

    def _get_signal(self):
        uri = f"{MiningHamsterSignalReceiver.BASE_URL}{self.key}"
        response = requests.get(uri)

        if response.ok:
            return response.json()[0]
        else:
            return None
