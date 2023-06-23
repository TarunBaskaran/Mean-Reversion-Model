import pandas as pd
import yfinance as yf
from tabulate import tabulate
import matplotlib.pyplot as plt
import os

# COLLECTS THE PRICING
symbol = input("INPUT YOUR STOCK TICKER HERE: ")
start_date = input("INPUT START DATE IN YYYY-MM-DD: ")
end_date = input("INPUT END DATE IN YYYY-MM-DD: ")
filename = f"{symbol}_data.csv"

# CHECK IF CSV ALREADY EXISTS
if os.path.isfile(filename):
    overwrite = input("CSV file already exists. Do you want to overwrite it? (y/n): ")
    if overwrite.lower() == 'y':
        data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date)['Close'])
        data.to_csv(filename)
    else:
        new_filename = input("Enter a new filename (or leave blank to append a suffix): ")
        if new_filename:
            filename = f"{new_filename}.csv"
        else:
            suffix = 1
            while os.path.isfile(filename):
                filename = f"{symbol}_data_{suffix}.csv"
                suffix += 1
            data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date)['Close'])
            data.to_csv(filename)
else:
    data = pd.DataFrame(yf.download(symbol, start=start_date, end=end_date)['Close'])
    data.to_csv(filename)

# COMPUTES THE MEANS
mean_price = data['Close'].mean()
std_price = data['Close'].std()

# MEAN FORMATTING
table = [["Mean Price", mean_price], ["Standard Deviation", std_price]]
table_str = tabulate(table, headers=["Metric", "Value"], tablefmt="fancy_grid")

print(table_str)

## TRADING SIGNALS
num_std_threshold = 1.5
data['Signal'] = 0  
data.loc[data['Close'] < (mean_price - num_std_threshold * std_price), 'Signal'] = 1  # BUYING SIGNALS
data.loc[data['Close'] > (mean_price + num_std_threshold * std_price), 'Signal'] = -1  # SELLING SIGNALS

print("Trading Signals:")
print(data['Signal'])

# BACKTESTING THE CODE
capital = 100000  
position = 0  # INITIAL POSITION 
shares_to_buy = 0  
portfolio_values = []  # THIS LIST STORES PORTFOLIO VALUES

for index, row in data.iterrows():
    if row['Signal'] == 1 and position != 1:  # BUY SIGNAL
        shares_to_buy = capital / row['Close']
        capital -= shares_to_buy * row['Close']
        position = 1
    elif row['Signal'] == -1 and position != -1:  # SELL SIGNAL
        capital += shares_to_buy * row['Close']
        shares_to_buy = 0
        position = -1

    # PORTFOLIO VALUE
    portfolio_value = capital + (shares_to_buy * row['Close'])
    portfolio_values.append(portfolio_value)

print("Final Portfolio Value:", portfolio_value)

# PLOTTING PORTFOLIO VALUE
plt.figure(figsize=(12, 8)) 
plt.plot(data.index, portfolio_values)
plt.xticks(rotation=45)
plt.title("Portfolio Value Over Time", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Portfolio Value", fontsize=12)
plt.grid(True)
plt.tight_layout()  
plt.show()
