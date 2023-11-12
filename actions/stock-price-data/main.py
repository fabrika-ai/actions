from pydantic import BaseModel

from fastapi import FastAPI, Depends
import functions_framework
import yfinance as yf

from helpers.utils import as_cloud_function

app = FastAPI()


class StockQueryParams(BaseModel):
    ticker: str
    period: str = "1d"  # e.g., "1d", "1mo", "1y"
    interval: str = "1d"  # e.g., "1m", "1d", "1wk"


@app.get("/stock/")
async def get_stock_data(params: StockQueryParams = Depends()):
    stock = yf.Ticker(params.ticker)
    # Fetching data based on the provided period (1mo) and interval (1d)
    hist = stock.history(period=params.period, interval=params.interval)
    if not hist.empty:
        # Returning all fetched data
        data = {
            "ticker": params.ticker,
            "data": hist.to_dict(orient="records")
        }
    else:
        data = {"error": "Insufficient data for ticker or period"}
    return data


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
