# Mean-Reversion Stock Trading Strategy

## DISCLAIMER
This script is provided for educational and informational purposes only. It does not constitute financial advice or recommendations. The use of this script to make real-time investment decisions is at your own risk. Always conduct thorough research and consult with a qualified financial advisor before making any investment decisions.

## Overview
This Python script implements a sophisticated mean-reversion stock trading strategy using historical pricing data. It calculates statistical measures, generates trading signals, and performs a comprehensive backtest to evaluate the strategy's performance.

## Prerequisites
To execute this script, ensure that the following libraries are installed:

pandas: Used for data manipulation and analysis.
yfinance: Enables retrieval of historical pricing data from Yahoo Finance.
tabulate: Facilitates the creation of formatted tables for displaying results.
matplotlib: Provides graphing capabilities for visualizing portfolio performance.

Install these libraries by running the following command:

```ruby
pip install pandas yfinance tabulate matplotlib
```

## Usage
Clone this repository or download the script file (trading_strategy.py) to your local machine.


Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script by executing the following command:

```ruby
python mean-revision-code.py
```

Enter the stock ticker symbol of the desired security when prompted, such as "AAPL" for Apple Inc.

Provide the start and end dates for the historical data analysis in the format "YYYY-MM-DD". For example, enter "2022-01-01" as the start date and "2022-12-31" as the end date.

The script will collect historical pricing data for the specified stock within the given date range.

Using the collected data, the script will calculate statistical measures, including the mean price and standard deviation of the stock's closing prices. These measures play a crucial role in identifying potential trading opportunities based on mean-reversion principles.

A table will be displayed, presenting the calculated statistical measures in a user-friendly format.

The script will generate trading signals based on the mean-reversion concept. These signals indicate whether to buy, sell, or hold the stock at specific points in time.

The generated trading signals will be displayed, providing valuable insights into potential trading opportunities and market behavior.

To evaluate the strategy's performance, the script will conduct an extensive backtest. This simulation involves making buying and selling decisions based on the generated trading signals. The final portfolio value will be presented, reflecting the effectiveness of the strategy within the specified timeframe.

Additionally, a line graph illustrating the portfolio value over time will be plotted and displayed. This visual representation allows for a comprehensive analysis of the strategy's performance trajectory.


