from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
from dashboard import expenditureDistribution

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
  return {"Welcome Data"}

@app.get("/dashboard_last_personal_list")
def get_expenditure_distribution():
    return expenditureDistribution()

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#   return{"item_id": item_id, "q": q} 

# @app.get("/yearData/{year_id}")
# async def read_year(year_id: int, user_id: int):
#   return{"year_id": year_id}

#api doc at 127.0.0.1:8000/docs (swagger)

# getBudgetAndCurrencyAskForCurrencyConversion()