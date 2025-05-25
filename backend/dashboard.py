import csv
from pandas import *
import os

def expenditureDistribution():
    filename = 'personal_financial_data.csv'
    data = []

    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames

            first_column = fieldnames[0]

            for row in reader:
                if first_column in row:
                    del row[first_column]
                data.append(row)
    except csv.Error as e:
        print(f"CSV read error: {e}")
        return {"error": "Failed to read CSV file."}
    except FileNotFoundError:
        return {"error": f"{filename} not found."}
    
    return data

def getExpensesByCategory():
    filename = 'personal_financial_data.csv'
    bill = None
    food = None
    taxes = None
    transport = None
    otherExpenses = None

    try:
        data = read_csv(filename)
        bill = sum(data['Bills'].tolist())
        food = sum(data['Food'].tolist())
        taxes = sum(data['Taxes'].tolist())
        transport = sum(data['Transport Expenses'].tolist())
        otherExpenses = sum(data['Other Expenses'].tolist())
    except csv.Error as e:
        print(f"CSV read error: {e}")
        return {"error": "Failed to read CSV file."}
    except FileNotFoundError:
        return {"error": f"{filename} not found."}
    
    return bill, food, taxes, transport, otherExpenses