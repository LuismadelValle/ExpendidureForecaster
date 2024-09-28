# import pandas as pd
# from pandas import DataFrame

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
# df = DataFrame({'Primer Mes': expenditure1, 'Segundo Mes': expenditure2, 'Promedio': averageExpenditure})

# df.to_excel('test.xlsx', sheet_name='Testing', index=False) install pandas on monday

print(f"Tus gastos promedio son {averageExpenditure}")