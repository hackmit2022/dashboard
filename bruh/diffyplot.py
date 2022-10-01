from urls import get_difficulty
from data import Difficulty
import plotly.express as px


d = Difficulty(**get_difficulty())

print(d)
x, y = tuple(zip(*d.values))

fig = px.bar(x=x, y=y)
fig.write_html("first_figure.html", auto_open=True)
