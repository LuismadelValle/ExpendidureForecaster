# import pandas as pd
# from pandas import DataFrame

amountOfMonthsToAverage = int(input("Cuantos meses desea controlar? "))
lst = list(map(int, input(f"Ingrese los gastos de los ultimos {amountOfMonthsToAverage} meses ").strip().split()))[:amountOfMonthsToAverage]

averageExpenditure = sum(lst)/amountOfMonthsToAverage

# df = DataFrame({'Primer Mes': expenditure1, 'Segundo Mes': expenditure2, 'Promedio': averageExpenditure})

# df.to_excel('test.xlsx', sheet_name='Testing', index=False) install pandas on monday

print(f"Tus gastos promedio son {averageExpenditure}")