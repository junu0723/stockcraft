# Show top 10 KOSPI stocks in yesterday
# Import pykrx, seaborn and matplotlib
import pykrx
import seaborn as sns
import matplotlib.pyplot as plt

# Get the trading volume of all KOSPI stocks on the previous day
df = pykrx.stock.get_market_ohlcv_by_ticker("20210714", market="KOSPI")

# Sort the dataframe by trading volume in descending order
df = df.sort_values(by="거래량", ascending=False)

# Select the top 10 items
df = df.head(10)

# Reset the index and rename the columns
df = df.reset_index()
df.columns = ["Ticker", "Open", "High", "Low",
              "Close", "Volume", "Value", "Change"]

# Get the ticker names
df["Name"] = df["Ticker"].apply(pykrx.stock.get_market_ticker_name)

# Plot a bar chart with seaborn
sns.barplot(x="Name", y="Volume", data=df)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()
