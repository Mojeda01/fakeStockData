import pandas as pd
import numpy as np

def format_decimal_separator(df):
    """ Formats the decimal separator in the DataFrame from '.' to ','."""
    return df.map(lambda x: f'{x:.2f}'.replace(".",",")) 

def generate_data(trading_days, years, companyA, companyB, companyC, stock_price):
    # generate date range
    dates = pd.date_range(start="24-01-01", periods=years * trading_days, freq="B")
    # Define company names
    companies = ["CompanyA", "CompanyB", "CompanyC"]
    #Initialize a DataFrame to store stock prices
    stock_data = pd.DataFrame(index=dates)

    # Generate random stock prices for each company
    for company in companies:
        # Simulate daily returns - normally distributed with mean=0 and std of 0.02 (2%)
        daily_returns = np.random.normal(0,0.02, size=(len(dates),))

        # Calculate the price series
        price_series = [stock_price]
        for return_ in daily_returns:
            price_series.append(price_series[-1] * (1 + return_))

        stock_data[company] = price_series[1:]

    formatted_stock_data = format_decimal_separator(stock_data)

    # Export the data to a CSV file
    file_name = "simulated_stock_data.csv"
    formatted_stock_data.to_csv(file_name, sep=";", decimal=",")
    msg = f"Data exported to {file_name}"

    return msg 
