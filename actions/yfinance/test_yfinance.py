from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock

from actions.yfinance.main import app

client = TestClient(app)


def test_get_stock_data_success():
    mock_response = MagicMock()
    mock_response.empty = False
    mock_response.to_dict.return_value = [{"dummy": "data"}]

    with patch('yfinance.Ticker') as mock_ticker:
        mock_ticker.return_value.history.return_value = mock_response
        response = client.get("/history/?ticker=AAPL&period=1d&interval=1d")
        assert response.status_code == 200
        assert response.json() == {
            "ticker": "AAPL",
            "data": [{"dummy": "data"}],
            "error": None
        }


def test_get_stock_data_incorrect_input():
    mock_response = MagicMock()
    mock_response.empty = True

    with patch('yfinance.Ticker') as mock_ticker:
        mock_ticker.return_value.history.return_value = mock_response
        response = client.get("/history/?ticker=AAPL&period=1d&interval=1w")
        assert response.status_code == 200
        assert response.json() == {
            "ticker": None,
            "data": None,
            "error": "Insufficient data for ticker or period"
        }
