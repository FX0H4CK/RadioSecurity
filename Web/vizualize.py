#!/usr/bin/python3

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('./Interface/SSIDs.html', mode="inline")
wifi = pd.read_csv('../Wifi/Raw/SSIDs.csv')
wifi.columns.tolist()

p = figure()
p.circle(x=' Speed', y=' ESSID', source=wifi, size=10, color='green')
p.title.text = 'SSIDs'
show(p)
