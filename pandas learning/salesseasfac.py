import pandas as pd
from pandas.core.arrays import integer
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
print("Setup Complete")


house_data = pd.read_excel("/Users/shivani/Downloads/2022 NLC -- Data Analysis Datasets/1 Houses Sold.xls",sheet_name = 2, header=[3,4], skipfooter=10, parse_dates=True, na_values='(NA)')
print(house_data.head(50))
#quit()
house_data.columns = ["Period", "US", "NE", "MW", "S", "W", "New Houses for Sale", "Months's supply"]
#house_data.fillna(method='bfill')
print(house_data.head(50))
plt.figure(figsize=(14,6))

# Add title
plt.title("Seasonal Indexes Used to Adjust Housing Units Sold and For Sale")

sns.lineplot(data=house_data.set_index('Period')[["NE", "US"]])
plt.show()