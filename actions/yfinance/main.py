from typing import List, Dict, Any, Optional

from pydantic import BaseModel

from fastapi import FastAPI, Depends
import functions_framework
import yfinance as yf

from helpers.utils import as_cloud_function

app = FastAPI()


class StockQueryParams(BaseModel):
    ticker: str  # Stock ticker symbol
    period: str = "1d"  # Time period for the stock data, e.g., "1d", "1mo", "1y"
    interval: str = "1d"  # Data interval, e.g., "1m", "1d", "1wk"


class StockDataResponse(BaseModel):
    ticker: Optional[str] = None  # Stock ticker symbol
    data: Optional[List[Dict[str, Any]]] = None  # Response Data
    error: Optional[str] = None  # Error


@app.get("/history/", response_model=StockDataResponse, summary="Get Stock History",
         description="Retrieves historical stock data based on ticker, period, and interval.")
async def get_stock_data(params: StockQueryParams = Depends()):
    stock = yf.Ticker(params.ticker)
    hist = stock.history(period=params.period, interval=params.interval)
    if not hist.empty:
        return StockDataResponse(ticker=params.ticker, data=hist.to_dict(orient="records"))
    else:
        return StockDataResponse(error="Insufficient data for ticker or period")


@functions_framework.http
def fastapi_func(request):
    return as_cloud_function(app, request)
