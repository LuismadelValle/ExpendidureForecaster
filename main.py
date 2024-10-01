from typing import Union
from fastapi import FastAPI
# from projectIdea import *

app = FastAPI()

@app.get("/")
def read_root():
  return {"Welcome Data"}

@app.get("dashboardData/")
async def getDashboardData(user_id: int):
  return{"user_id": user_id}

@app.get("items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
  return{"item_id": item_id, "q": q} 

@app.get("yearData/{year_id}")
async def read_year(year_id: int, user_id: int):
  return{"year_id": year_id}

#api doc at 127.0.0.1:8000/docs (swagger)

# getBudgetAndCurrencyAskForCurrencyConversion()