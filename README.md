# fake stock data - Stock Market Data Simulation Program
####

![Example Image](https://github.com/Mojeda01/fakeStockData/blob/main/Example%20Image/example.png)


Purpose:
- This program is designed to simulate stock market data for a specified period. It generates synthetic daily stock prices for a given set of companies over a period of five years.

Methodology:
- The program uses  a random walk model to simulate daily stock price movements. This model is a simply yet common method in financial simulations.
- It starts with an initial stock price (e.g., 100) and then applies simulated daily returns to this price.
- Daily returns are generated using an normal distribution with a mean of 0 and a specified standard deviation (e.g., 0.02, representing a 2% maximul daily change).
- The simulated daily returns are applied sequentially to generate  a time series of stock prices for each company.
- The program uses the pandas library for data handling and the numpy library for numerical operations.

Output:
- The output is a CSV file named 'simulated_stock_data.csv'. This file contains simulated daily stock prices for each company over the five-year period.
- The dataset includes a date column and separate columm amd seprate columns for each company's stock prices.
- The decimal separator in the output file is formatted as a comma (",") instead of a period (".").

Usage Note:
- The generated data is entirely synthetic and intended for simulation purposes only. It should not be used for real-world trading or investment decisions.
- The random walk model is a basic simulation approach and does not account for the complexities of actual stock market behavior.

Dependencies:
- pandas: For data manipulation and export.
- numpy: For numerical operations and random number generation.

Author: Marco Å. Ojeda

Date: 17.01.2024
