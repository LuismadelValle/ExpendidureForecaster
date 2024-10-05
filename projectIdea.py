import pandas as pd
from pandas import DataFrame

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

  df = pd.DataFrame(expenditureList)
  df.to_excel('test.xlsx', sheet_name='Testing', index=False) 

  print(f"Dataframe {df}  {averageExpenditure}")

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
  
defineExpendituresCategories()
averageExpenditures()