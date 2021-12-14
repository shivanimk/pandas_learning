import pandas as pd
from pandas.core.arrays import integer
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")


house_data = pd.read_excel("/Users/shivani/Downloads/2022 NLC -- Data Analysis Datasets/2 Houses for Sale.xls",header=[8,9], skipfooter=4, parse_dates=True, na_values='(NA)')
print(house_data.head(50))
#quit()
house_data.columns = ["Period", "US", "NE", "MW", "S", "W"]
#house_data.fillna(method='bfill')
print(house_data.head(50))
plt.figure(figsize=(14,6))

# Add title
plt.title("Houses for Sale by Region")

sns.lineplot(data=house_data.set_index('Period'))
plt.show()