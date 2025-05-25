from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
from dashboard import *
from budgets import *

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

@app.get("/api/dashboard_last_personal_list")
def get_expenditure_distribution():
    return expenditureDistribution()

@app.get("/api/expenditures")
def get_ExpendituresSum():
   return getExpensesByCategory()

@app.get("/api/personalForecast/arimaModel")
def incomeForecastArima():
  return personalIncomeForecast()

@app.get("/api/personalForecast/sarimaxModel")
def incomeForecastSarimax():
  return personalIncomeForecastSarimax()

@app.get("/api/personalForecast/expendArimaModel")
def expendForecastArima():
  return personalExpenditureForecastArima()

@app.get("/api/personalForecast/expenditureSarimaxModel")
def expenditureForecastSarimax():
  return personalExpenditureForecastSarimax()

@app.get("/api/personalForecast/savingsArimaModel")
def savingsForecastArima():
  return personalSavingsForecastArima()

@app.get("/api/personalForecast/savingsSarimaxModel")
def savingsForecastSarimax():
  return personalSavingsForecastSarimax()

# @app.get("/yearData/{year_id}")
# async def read_year(year_id: int, user_id: int):
#   return{"year_id": year_id}


