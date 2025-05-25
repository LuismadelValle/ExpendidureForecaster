import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

def personalIncomeForecast():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)

        df["Month"] = pd.to_datetime(df["Month"])
        df.set_index("Month", inplace=True)

        income_series = df["Income from Work"]

        train = income_series[:-12]
        test = income_series[-12:]

        model = ARIMA(train, order=(5, 1, 0))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        mae = mean_absolute_error(test, forecast)
        mse = mean_squared_error(test, forecast)
        rmse = np.sqrt(mse)

    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
    
def personalIncomeForecastSarimax():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)

        df["Month"] = pd.to_datetime(df["Month"])
        df.set_index("Month", inplace=True)

        income_series = df["Income from Work"]

        train = income_series[:-12]
        test = income_series[-12:]

        sarimax_model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12)) 
        sarimax_result = sarimax_model.fit()
        sarimax_forecast = sarimax_result.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, sarimax_forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        sarimax_mae = mean_absolute_error(test, sarimax_forecast)
        sarimax_mse = mean_squared_error(test, sarimax_forecast)
        sarimax_rmse = np.sqrt(sarimax_mse)

    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
    
def personalExpenditureForecastArima():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)
        expense_columns = ["Bills", "Food", "Taxes", "Transport Expenses", "Other Expenses"]

        df["Month"] = pd.to_datetime(df["Month"])      
        df["Total Expenses"] = df[expense_columns].sum(axis=1)

        expenses_series = df["Total Expenses"]

        train = expenses_series[:-12]
        test = expenses_series[-12:]

        sarimax_model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12)) 
        sarimax_result = sarimax_model.fit()
        sarimax_forecast = sarimax_result.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        sarimax_mae = mean_absolute_error(test, sarimax_forecast)
        sarimax_mse = mean_squared_error(test, sarimax_forecast)
        sarimax_rmse = np.sqrt(sarimax_mse)
    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
    
def personalExpenditureForecastSarimax():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)
        expense_columns = ["Bills", "Food", "Taxes", "Transport Expenses", "Other Expenses"]

        df["Month"] = pd.to_datetime(df["Month"])      
        df["Total Expenses"] = df[expense_columns].sum(axis=1)

        expenses_series = df["Total Expenses"]

        train = expenses_series[:-12]
        test = expenses_series[-12:]

        model = ARIMA(train, order=(5, 1, 0))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        mae = mean_absolute_error(test, forecast)
        mse = mean_squared_error(test, forecast)
        rmse = np.sqrt(mse)
    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
    
def personalSavingsForecastArima():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)

        df["Month"] = pd.to_datetime(df["Month"])
        df.set_index("Month", inplace=True)

        income_series = df["Savings"]

        train = income_series[:-12]
        test = income_series[-12:]

        model = ARIMA(train, order=(5, 1, 0))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        mae = mean_absolute_error(test, forecast)
        mse = mean_squared_error(test, forecast)
        rmse = np.sqrt(mse)

    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}
    
def personalSavingsForecastSarimax():
    filename = 'personal_financial_data.csv'

    try:
        df = pd.read_csv(filename)

        df["Month"] = pd.to_datetime(df["Month"])
        df.set_index("Month", inplace=True)

        income_series = df["Savings"]

        train = income_series[:-12]
        test = income_series[-12:]

        sarimax_model = SARIMAX(train, order=(1,1,1), seasonal_order=(1,1,1,12)) 
        sarimax_result = sarimax_model.fit()
        sarimax_forecast = sarimax_result.forecast(steps=12)

        plt.figure(figsize=(10, 5))
        plt.plot(train, label='Train')
        plt.plot(test, label='Test')
        plt.plot(test.index, sarimax_forecast, label='Forecast')
        plt.legend()
        plt.title('ARIMA Forecasting')
        plt.show()

        sarimax_mae = mean_absolute_error(test, sarimax_forecast)
        sarimax_mse = mean_squared_error(test, sarimax_forecast)
        sarimax_rmse = np.sqrt(sarimax_mse)

    except pd.errors.EmptyDataError:
        print("CSV is empty or corrupted.")
        return {"error": "CSV is empty or corrupted."}
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return {"error": f"{filename} not found."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}