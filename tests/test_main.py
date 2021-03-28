from unittest.mock import Mock, patch
from main import get_signal


@patch("main.requests.get")
def test_MH_buy_request_reponse(mock_get):
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
    actual = get_signal()

    assert actual == expected


@patch("main.requests.get")
def test_failed_MH_request_reponse(mock_get):
    mock_get.return_value = Mock(ok=False)
    mock_get.return_value.json.return_value = None

    actual = get_signal()

    assert actual == None
