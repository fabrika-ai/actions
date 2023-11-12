from pydantic import BaseModel

from fastapi import FastAPI, Depends
import functions_framework
import yfinance as yf

from helpers.utils import as_cloud_function

app = FastAPI()


class StockQueryParams(BaseModel):
    period: str = "1d"  # e.g., "1d", "1mo", "1y"
    interval: str = "1d"  # e.g., "1m", "1d", "1wk"
    data_points: int = 5  # Number of last data points


@app.get("/stock/{ticker}")
async def get_stock_data(ticker: str, params: StockQueryParams = Depends()):
    stock = yf.Ticker(ticker)
    # Fetching data based on the provided period and interval
    hist = stock.history(period=params.period, interval=params.interval)
    if not hist.empty and len(hist) >= params.data_points:
        # Fetching the last 'data_points' number of entries
        latest_data = hist.iloc[-params.data_points:]
        data = {
            "ticker": ticker,
            "data": latest_data.to_dict(orient="records")
        }
    else:
        data = {"error": "Insufficient data for ticker or period"}
    return data


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
