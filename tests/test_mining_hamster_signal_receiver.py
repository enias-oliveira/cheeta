from pytest import fixture
from unittest.mock import Mock, patch

from src.market_hypothesis_receiver import MarketHypothesisReceiver


@fixture
def test_mhl():
    test_mh_api_key = "288b2113-28ac-4b14-801f-f4d9cf9d87ad"
    return MarketHypothesisReceiver(
        mining_hamster=True, mining_hamster_key=test_mh_api_key
    )


@patch("src.market_hypothesis_receiver.requests.get")
def test_MH_request_buy_signal_reponse(mock_get, test_mhl):
    mock_signal = [
        {
            "market": "BTC-CELR",
            "lastprice": "0.00000166",
            "signalmode": "buy",
            "exchange": "binance",
            "basevolume": 1133.46104551,
            "time": "2021-03-28 08:05:02",
            "signal_id": "bin_1924329646",
            "signals_qty": 29,
            "profit_avg": 16.00,
            "profit_median": 12.80,
            "profit_mode": 6.40,
            "profit_mode_qty": 4,
        }
    ]
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_signal

    expected = {
        "market": "BTC-CELR",
        "lastprice": "0.00000166",
        "signalmode": "buy",
        "exchange": "binance",
        "basevolume": 1133.46104551,
        "time": "2021-03-28 08:05:02",
        "signal_id": "bin_1924329646",
        "signals_qty": 29,
        "profit_avg": 16.00,
        "profit_median": 12.80,
        "profit_mode": 6.40,
        "profit_mode_qty": 4,
    }
    actual = test_mhl._get_mining_hamster_signal()

    assert actual == expected


@patch("src.market_hypothesis_receiver.requests.get")
def test_MH_request_sell_signal_reponse(mock_get, test_mhl):
    mock_signal = [
        {
            "market": "BTC-CELR",
            "lastprice": "0.00000166",
            "signalmode": "sell",
            "exchange": "binance",
            "basevolume": 1133.46104551,
            "time": "2021-03-28 08:05:02",
            "signal_id": "bin_1924329646",
            "signals_qty": 29,
            "profit_avg": 16.00,
            "profit_median": 12.80,
            "profit_mode": 6.40,
            "profit_mode_qty": 4,
        }
    ]
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = mock_signal

    expected = {
        "market": "BTC-CELR",
        "lastprice": "0.00000166",
        "signalmode": "sell",
        "exchange": "binance",
        "basevolume": 1133.46104551,
        "time": "2021-03-28 08:05:02",
        "signal_id": "bin_1924329646",
        "signals_qty": 29,
        "profit_avg": 16.00,
        "profit_median": 12.80,
        "profit_mode": 6.40,
        "profit_mode_qty": 4,
    }
    actual = test_mhl._get_mining_hamster_signal()

    assert actual == expected


@patch("src.market_hypothesis_receiver.requests.get")
def test_failed_MH_request_reponse(mock_get, test_mhl):
    mock_get.return_value = Mock(ok=False)
    mock_get.return_value.json.return_value = None

    actual = test_mhl._get_mining_hamster_signal()
    expected = None

    assert actual == expected
