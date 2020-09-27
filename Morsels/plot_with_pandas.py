# Plot with pandas from RealPython
import pandas as pd
import matplotlib.pyplot as plt

download_url = (
                "https://raw.githubusercontent.com/fivethirtyeight/"
                "data/master/college-majors/recent-grads.csv"
               )
df = pd.read_csv(download_url)
# print(f"{type(df)}")
# pd.set_option("display.max.columns", None)
#
# print(f"{df.head()}")

df.plot(x="Rank", y=["P25th", "Median", "P75th"])
plt.show()
