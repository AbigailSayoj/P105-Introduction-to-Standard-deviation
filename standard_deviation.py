import csv

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

total = 0
n = len(file_data)

for data in file_data:
    total += float(data[1])

mean = total / n
print("Mean / Average => " + str(mean))

import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")

fig = px.scatter(df,    x = "Number of data",
                        y = "Data"
            )
fig.update_layout(shapes = [
    dict(
      type = 'line',
      y0 = mean, y1 = mean,
      x0 = 0, x1 = n
    )
])

fig.update_yaxes(rangemode = "tozero")

fig.show()