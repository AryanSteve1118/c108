import pandas as pd
import plotly.figure_factory as puf
import csv

keldeo=pd.read_csv("data.csv")
virizion=keldeo["Marks In Percentage"].tolist()
terrakion=puf.create_distplot([virizion],["cobalion"],show_hist=False)
terrakion.show()