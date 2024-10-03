import pandas as pd
from pandas import DataFrame

def budget(amount, currency):
  global budgetForCurrentMonth
  budgetForCurrentMonth = int(amount)
  global budgetCurrency
  budgetCurrency = currency

def averageExpenditures():
  expenditureList = []
  amountOfMonthsToAverage = int(input("Cuantos meses desea controlar? "))

  print(f"Desglose sus gastos en alquiler(1), facturas(2), comida(3) y otros(4)")

  currentMonth = 1
  for i in range(amountOfMonthsToAverage):
    iRange = 1
    tempList = []
    for j in range (4):
      element = int(input(f"Gastos en {iRange} para el mes {currentMonth} "))
      iRange = iRange + 1
      tempList.append(element)
    currentMonth = currentMonth + 1
    expenditureList.append(tempList)

  averageExpenditure = sum(sum(expenditureList, []))/amountOfMonthsToAverage

  df = pd.DataFrame(expenditureList)
  df.to_excel('test.xlsx', sheet_name='Testing', index=False) 

  print(f"Dataframe {df}")

def currencyConversion(amountFirstCoin, currencyDenomination, conversionRate):
  convertedCurrency = int(amountFirstCoin)*float(conversionRate)
  print(f"The change for {amountFirstCoin}{currencyDenomination} at the current exchange rate is {convertedCurrency}")

def getBudgetAndCurrencyAskForCurrencyConversion():
  budgetAmount = input("Ingrese el total de su presupuesto ")
  budgetCurrency = input("Ingrese la moneda en la que esta su presupuesto ")
  convertBudgetToOtherCurrency = input("Desea convertir su presupuesto a otra denominacion? (y/n) ")
  budget(budgetAmount, budgetCurrency)

  if convertBudgetToOtherCurrency == 'y':
    currencyConversionRate = input(f"Ingrese la tasa de cambio ")
    currencyConversion(budgetAmount, budgetCurrency, currencyConversionRate)
  elif convertBudgetToOtherCurrency == 'n':
    print(f"Presupuesto registrado de {budgetAmount} {budgetCurrency}")
  else:
    raise Exception("Responder con y o n")

averageExpenditures()  