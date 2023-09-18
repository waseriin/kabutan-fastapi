from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()
scraper = Scraper()

@app.get("/{stock_code}")
async def kabutan(stock_code):
  return scraper.kabutan_search(stock_code)
