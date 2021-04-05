from pytest import fixture
from unittest.mock import Mock, patch

from src.mining_hamster_signal_receiver import MiningHamsterSignalReceiver
from src.market_hypothesis import MarketHypothesis


@fixture
def test_mhsr():
    test_mh_api_key = "288b2113-28ac-4b14-801f-f4d9cf9d87ad"
    return MiningHamsterSignalReceiver(test_mh_api_key)


@fixture
def mock_buy_signal():
    return [
        {
            "market": "BTC-BNB",
            "lastprice": "0.0058221",
            "signalmode": "buy",
            "exchange": "binance",
            "basevolume": 889654.46104551,
            "time": "2021-04-03 23:55:02",
            "signal_id": "bin_1924329646",
            "signals_qty": 29,
            "profit_avg": 16.00,
            "profit_median": 12.80,
            "profit_mode": 6.40,
            "profit_mode_qty": 4,
        }
    ]


@fixture
def mock_sell_signal():
    return [
        {
            "market": "BTC-BNB",
            "lastprice": "0.0058221",
            "signalmode": "sell",
            "exchange": "binance",
            "basevolume": 889654.46104551,
            "time": "2021-04-03 23:55:02",
            "signal_id": "bin_1924329646",
            "signals_qty": 29,
            "profit_avg": 16.00,
            "profit_median": 12.80,
            "profit_mode": 6.40,
            "profit_mode_qty": 4,
        }
    ]


@patch("src.mining_hamster_signal_receiver.requests.get")
def test_request_buy_signal_reponse(mock_get, test_mhsr, mock_buy_signal):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_buy_signal

    expected = {
        "market": "BTC-BNB",
        "lastprice": "0.0058221",
        "signalmode": "buy",
        "exchange": "binance",
        "basevolume": 889654.46104551,
        "time": "2021-04-03 23:55:02",
        "signal_id": "bin_1924329646",
        "signals_qty": 29,
        "profit_avg": 16.00,
        "profit_median": 12.80,
        "profit_mode": 6.40,
        "profit_mode_qty": 4,
    }
    actual = test_mhsr._get_signal()

    assert actual == expected


@patch("src.mining_hamster_signal_receiver.requests.get")
def test_request_sell_signal_reponse(mock_get, test_mhsr, mock_sell_signal):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_sell_signal

    expected = {
        "market": "BTC-BNB",
        "lastprice": "0.0058221",
        "signalmode": "sell",
        "exchange": "binance",
        "basevolume": 889654.46104551,
        "time": "2021-04-03 23:55:02",
        "signal_id": "bin_1924329646",
        "signals_qty": 29,
        "profit_avg": 16.00,
        "profit_median": 12.80,
        "profit_mode": 6.40,
        "profit_mode_qty": 4,
    }
    actual = test_mhsr._get_signal()

    assert actual == expected


@patch("src.mining_hamster_signal_receiver.requests.get")
def test_failed_request_reponse(mock_get, test_mhsr):
    mock_get.return_value = Mock(ok=False)
    mock_get.return_value.json.return_value = None

    actual = test_mhsr._get_signal()
    expected = None

    assert actual == expected


@patch("src.mining_hamster_signal_receiver.requests.get")
def test_start_receiver_buy_signal(mock_get, test_mhsr, mock_buy_signal, capsys):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_buy_signal

    expected_captured_listening = "Listening to Mining Hamster\nSignal Received\nProcessing...\nHypothesis: buy - BNB/BTC\nExchange: binance\nPrice: 0.0058221\n"

    test_mhsr.start_receiver()
    actual_captured_listening = capsys.readouterr().out

    assert actual_captured_listening == expected_captured_listening


@patch("src.mining_hamster_signal_receiver.requests.get")
def test_start_receiver_no_signal(mock_get, test_mhsr, capsys, mock_buy_signal):
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_buy_signal
    test_mhsr.last_buy_signal_id = "bin_1924329646"

    expected_captured_listening = "Listening to Mining Hamster\n"

    test_mhsr.start_receiver()
    actual_captured_listening = capsys.readouterr().out

    assert actual_captured_listening == expected_captured_listening


def test_convert_signal_to_MH():
    given_buy_signal = {
        "market": "BTC-BNB",
        "lastprice": "0.0058221",
        "signalmode": "buy",
        "exchange": "binance",
        "basevolume": 889654.46104551,
        "time": "2021-04-03 23:55:02",
        "signal_id": "bin_1924329646",
        "signals_qty": 29,
        "profit_avg": 16.00,
        "profit_median": 12.80,
        "profit_mode": 6.40,
        "profit_mode_qty": 4,
    }

    expected_market_hypothesis = MarketHypothesis(
        market="BTC",
        trading_pair="BNB",
        side=given_buy_signal["signalmode"],
        price=given_buy_signal["lastprice"],
        exchange=given_buy_signal["exchange"],
        volume=given_buy_signal["basevolume"],
        hypothesis_id=given_buy_signal["signal_id"],
    ).__dict__

    actual_market_hypothesis = MiningHamsterSignalReceiver._convert_signal_to_MH(
        given_buy_signal
    ).__dict__

    assert actual_market_hypothesis == expected_market_hypothesis
