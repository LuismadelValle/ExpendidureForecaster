import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

from tqdm.notebook import tqdm
from statsmodels.graphics.tsaplots import plot_acf

from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import RFECV
from sklearn.ensemble import  HistGradientBoostingRegressor
from skforecast.ForecasterAutoregMultiSeries import ForecasterAutoregMultiSeries
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.model_selection import backtesting_forecaster
from skforecast.model_selection import bayesian_search_forecaster
from skforecast.model_selection_multiseries import backtesting_forecaster_multiseries
from skforecast.model_selection_multiseries import bayesian_search_forecaster_multiseries
from skforecast.model_selection_multiseries import select_features_multiseries
from skforecast.plot import set_dark_theme
from skforecast.preprocessing import series_long_to_dict
from skforecast.preprocessing import exog_long_to_dict

def budget(amount, currency):
  global budgetForCurrentMonth
  budgetForCurrentMonth = int(amount)
  global budgetCurrency
  budgetCurrency = currency

def defineExpendituresCategories():
  global expenditureCategories
  expenditureCategories = []
  totalCategories = int(input(f"En cuantas categorias desea desglosar sus gastos mensuales? "))

  for i in range(totalCategories):
    category = input(f"Ingrese el nombre de la categoria ")
    expenditureCategories.append(category)
  
def averageExpenditures():
  global expenditureList
  expenditureList = []
  amountOfMonthsToAverage = int(input("Cuantos meses desea controlar? "))
  totalCategories = len(expenditureCategories)

  currentMonth = 1
  for i in range(amountOfMonthsToAverage):
    iRange = 0
    tempList = []
    for j in range (totalCategories):
      element = int(input(f"Gastos para {expenditureCategories[iRange]} para el mes {currentMonth} "))
      iRange = iRange + 1
      tempList.append(element)
    currentMonth = currentMonth + 1
    expenditureList.append(tempList)

  averageExpenditure = sum(sum(expenditureList, []))/amountOfMonthsToAverage
  print(f"Tus gastos promedio para estos ultimos {amountOfMonthsToAverage} es {averageExpenditure}")

def exportData():
  global df
  df = pd.DataFrame(expenditureList)
  df.to_excel('test.xlsx', sheet_name='Testing', index=False)

def predictExpenditures(): #definir modelos a usar 
  trainingData = pd.read_csv('trainingData.csv')
  exog = pd.read_csv('trainingData.csv')
  trainingData['timestamp'] = pd.to_datetime(trainingData['Date'])
  exog['timestamp'] = pd.to_datetime(exog['Date'])

  display(trainingData.head())
  print("")
  display(exog.head())

  # train = trainingData.iloc[:-12] 
  # test = trainingData.iloc[-12:]

  # arima_model = ARIMA(train, order=(5,1,0))
  # arima_result = arima_model.fit()

  # arima_forecast = arima_result.forecast(steps=12)

  # sarimax_model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12)) 
  # sarimax_result = sarimax_model.fit()
  # sarimax_forecast = sarimax_result.forecast(steps=12)

  # plt.figure(figsize=(10, 5))
  # plt.plot(train, label='Train')
  # plt.plot(test, label='Test')
  # plt.plot(arima_forecast, label='ARIMA Forecast')
  # plt.plot(sarimax_forecast, label='SARIMAX Forecast')
  # plt.legend()
  # plt.title('ARIMA and SARIMAX Forecasting')
  

  # #MAE
  # arima_mae = mean_absolute_error(test, arima_forecast)
  # sarimax_mae = mean_absolute_error(test, sarimax_forecast)
  # #RMSE
  # arima_mse = mean_squared_error(test, arima_forecast)
  # arima_rmse = np.sqrt(arima_mse)
  # sarimax_mse = mean_squared_error(test, sarimax_forecast)
  # sarimax_rmse = np.sqrt(sarimax_mse)
  # print(f"ARIMA MAE: {arima_mae:.2f}, SARIMAX MAE: {sarimax_mae:.2f}" )
  # print(f"ARIMA RMSE: {arima_rmse:.2f}, SARIMAX RMSE: {sarimax_rmse:.2f}")

  # plt.show()

def currencyConversion(amountFirstCoin, currencyDenomination, conversionRate):
  convertedCurrency = int(amountFirstCoin)*float(conversionRate)
  print(f"The change for {amountFirstCoin}{currencyDenomination} at the current exchange rate is {convertedCurrency}")

def getBudgetAndCurrencyAskForCurrencyConversion():
  budgetAmount = input(f"Ingrese el total de su presupuesto ")
  budgetCurrency = input(f"Ingrese la moneda en la que esta su presupuesto ")
  convertBudgetToOtherCurrency = input(f"Desea convertir su presupuesto a otra denominacion? (y/n) ")
  budget(budgetAmount, budgetCurrency)

  if convertBudgetToOtherCurrency == 'y':
    currencyConversionRate = input(f"Ingrese la tasa de cambio ")
    currencyConversion(budgetAmount, budgetCurrency, currencyConversionRate)
  elif convertBudgetToOtherCurrency == 'n':
    print(f"Presupuesto registrado de {budgetAmount} {budgetCurrency}")
  else:
    raise Exception("Responder con y o n")
  
def familyMembers(args):
  familyMembersBool = bool(args)
  global totalFamilyMembers 
  totalFamilyMembers = 0

  if familyMembersBool == True:
    totalFamilyMembers = int(input(f"Cuantos miembros tiene su familia "))
  elif familyMembersBool == False:
    exit
  else:
    raise Exception("familyMembersBool must be a boolean")
  
def familyMembersBudget():
  global membersBudget
  membersBudget = []
  familyMemberName = ''
  budgetForCurrentMonth = 0
  i = 0

  while i <= (totalFamilyMembers - 1):
    tempList = []
    familyMemberName = input(f"Nombre del familiar: ")
    budgetForCurrentMonth = float(input(f"Presupuesto de este mes para {familyMemberName} "))
    tempList.append(familyMemberName)
    tempList.append(budgetForCurrentMonth)
    membersBudget.append(tempList)
    i = i + 1   
  
predictExpenditures()