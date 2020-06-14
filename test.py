import plotille as pt
import numpy as np

X = np.sort(np.random.normal(size=1000))

fig = pt.Figure()
fig.width = 60
fig.height = 30
fig.set_x_limits(min_=-10, max_=10)
fig.set_y_limits(min_=-10, max_=10)


a = 4
b = 2
x_cord = -1
y_cord = -2
rot = np.radians(-30)
GRANULARITY = 0.2
e_x = [(a*np.cos(x_point)) for x_point in np.arange(0, (2*np.pi), GRANULARITY)]
e_y = [(b*np.sin(y_point)) for y_point in np.arange(0, (2*np.pi), GRANULARITY)]
e_x_r = [((e_x[i]*np.cos(rot))-(e_y[i]*np.sin(rot))) for i in range(len(e_x))]
e_y_r = [((e_x[i]*np.sin(rot))+(e_y[i]*np.cos(rot))) for i in range(len(e_y))]
e_x_m = [((e_x_r[i]+x_cord)) for i in range(len(e_x_r))]
e_y_m = [((e_y_r[i]+y_cord)) for i in range(len(e_y_r))]
fig.color_mode = 'byte'
fig.plot(e_x_m, e_y_m, lc=200, label='square')
import pdb; pdb.set_trace()
print(fig.show(legend=True))
