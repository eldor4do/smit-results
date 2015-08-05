##all imports
import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
from bokeh.plotting import figure, show, output_file, ColumnDataSource
pd.options.display.mpl_style = 'default'
from six.moves import zip
from bokeh.models import HoverTool
##end imports

def formData():
    file = "grade.txt"
    ranking = pd.read_table(file)
    print ranking
    return ranking
def mscatter(p, x, y, branch, c,typestr,source):
    p.scatter(x, y, marker=typestr,
            line_color="#6666ee", fill_color=c, fill_alpha=0.5, size=y*2,source = source)

ranking = formData()
data_to_plot = ranking.grade
xdata = data_to_plot.index
ydata = data_to_plot
branch = ranking.branch
name = ranking.name
#colour to seperate different branches. Colours from Pantone colour palette
colorName = {1:'#FE5000',5:'#44D62C',8:'#FFE900	',7:'#C6007E',9:'#003594',10:'#00C389',3:'#332F21'}
colors = [ colorName[(ord(y[0])*2 + ord(y[1]))%11] for y in branch ]

#for hover tool
source = ColumnDataSource(
    data=dict(
        name=name,
        branch=branch,
        cgpa=ydata
    )
)

hover = HoverTool(
    tooltips=[
        ("name", "@name"),
        ("branch", "@branch"),
        ("cgpa", "@cgpa"),
    ]
)
p = figure(title="CGPA of 4th year students",tools=[hover,'resize','reset','box_zoom'])
output_file("cgpa.html")
#plot the scatter plot
mscatter(p, xdata, ydata, branch,colors,"circle",source)
p.plot_height=600
p.plot_width=1200
p.background_fill = "snow"
p.xaxis.axis_label = "Index according to Registration No."
p.yaxis.axis_label = "CGPA"
p.yaxis.major_label_orientation = "vertical"
p.axis.axis_line_color = "yellow"
show(p)
