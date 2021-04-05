from src.market_hypothesis import MarketHypothesis

from pytest import fixture


@fixture
def test_market_hypothesis():
    given = {
        "exchange": "binance",
        "market": "BTC",
        "trading_pair": "BNB",
        "lastprice": "0.0058221",
        "signalmode": "buy",
        "exchange": "binance",
        "basevolume": 889654.46104551,
        "signal_id": "bin_1924329646",
    }
    return MarketHypothesis(
        market=given["market"],
        trading_pair=given["trading_pair"],
        side=given["signalmode"],
        price=given["lastprice"],
        exchange=given["exchange"],
        volume=given["basevolume"],
        hypothesis_id=given["signal_id"],
    )


def test_attributes(test_market_hypothesis):
    expected = {
        "market": "BTC",
        "trading_pair": "BNB",
        "side": "buy",
        "price": 0.0058221,
        "exchange": "binance",
        "volume": 889654.46104551,
        "hypothesis_id": "bin_1924329646",
        "risk_level": 1,
    }

    test_market_hypothesis._set_risk_level(1)
    actual = test_market_hypothesis.__dict__

    assert actual == expected


def test_calculate_risk_level(test_market_hypothesis):
    expected_risk_level = 1
    actual_risk_level = test_market_hypothesis._get_risk_level()

    assert actual_risk_level == expected_risk_level


def test_str(test_market_hypothesis, capsys):
    expected_str = "Hypothesis: buy - BNB/BTC\nExchange: binance\nPrice: 0.0058221\n"

    print(test_market_hypothesis)
    actual_str = capsys.readouterr().out

    assert actual_str == expected_str
