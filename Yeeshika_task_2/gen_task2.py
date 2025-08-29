from skyfield.api import EarthSatellite, load, utc
from datetime import datetime, timedelta
import numpy as np
import plotly.graph_objects as go
import streamlit as st

### data collection

st.title("Satellite trajectories for past 30 days")

tle_raw_data = [
  """NOAA 18                 
  1 28654U 05018A   25232.46363040  .00000076  00000+0  63584-4 0  9991
  2 28654  98.8395 311.1234 0013149 286.4823  73.4904 14.13628417 43905""",
  """NOAA 15                 
  1 25338U 98030A   25231.77009435  .00000153  00000+0  80310-4 0  9993
  2 25338  98.5336 255.1809 0010950 145.7140 214.4750 14.27013376418307""",
  """NAVSTAR 43 (USA 132)    
  1 24876U 97035A   25231.06188711 -.00000030  00000+0  00000+0 0  9998
  2 24876  55.8345 110.3944 0094273  55.6399 305.3151  2.005626452058""",
  """SWAS                    
  1 25560U 98071A   25232.31455899  .00002783  00000+0  19436-3 0  9996
  2 25560  69.8961 281.7543 0006976 334.4167  25.6649 15.06569329452161""",
  """STELLA                  
  1 22824U 93061B   25231.92620007 -.00000042  00000+0  15854-5 0  9990
  2 22824  98.8192 289.3899 0007046  41.0477   9.7317 14.27458147661794""",
  """COSMOS 1989 (ETALON 1)  
  1 19751U 89001C   25232.26812757  .00000018  00000+0  00000+0 0  9990
  2 19751  64.7694  82.4995 0023416 216.7852 315.1726  2.13156073285025""",
  """IRIS                    
  1 39197U 13033A   25231.57687540  .00001065  00000+0  13165-3 0  9994
  2 39197  97.9505  66.6828 0023900 222.8047 137.1307 14.84728440655629""",
  """GSAT-15                 
  1 41028U 15065A   25231.90989870 -.00000274  00000+0  00000+0 0  9997
  2 41028   0.1200 266.3297 0002518 204.9431 278.2718  1.00272223 35848""",
  """NOVA 2                  
  1 19223U 88052A   25231.64859329  .00000036  00000+0  65522-4 0  9991
  2 19223  89.9791  78.4690 0029665 333.9715  94.0814 13.22918213794261""",
  """POLAR                   
  1 23802U 96013A   25231.11455270  .00000276  00000+0  00000+0 0  9995
  2 23802  79.5167 230.3885 6177374 219.2751  73.7469  1.29846705140916"""
]

### loading time and getting x,y,z co-ordinates

ts = load.timescale()

tle_data = {}
for tle in tle_raw_data:
    lines = tle.strip().split('\n')
    name = lines[0].strip()
    line1 = lines[1].strip()
    line2 = lines[2].strip()
    tle_data[name] = EarthSatellite(line1, line2, name, ts)

start_date = datetime.now(tz=utc) - timedelta(days=30)
end_date = datetime.now(tz=utc)
delta = timedelta(hours=3)

times = []
current = start_date
while current <= end_date:
    times.append(ts.utc(current))
    current += delta

positions = {}
for name, sat in tle_data.items():
    x = []
    y = []
    z = []
    for t in times:
        geo = sat.at(t)
        pos = geo.position.km
        x.append(pos[0])
        y.append(pos[1])
        z.append(pos[2])
    positions[name] = (x, y, z)

st.write("Click to plot")
if st.button("Plot"):
### ploting


    colors = ['red', 'blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'yellow', 'pink', 'brown']


    orbit_lines = []
    for i, (name, (x, y, z)) in enumerate(positions.items()):  #orbital lines
        orbit_lines.append(go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='lines',
            line=dict(color=colors[i % len(colors)], width=0.5),
            name=f"{name} Orbit",
            opacity=0.4
        ))

    frames = []
    for k in range(len(times)):  #frames
        frame_data = []
        for i, (name, (x, y, z)) in enumerate(positions.items()):
            frame_data.append(go.Scatter3d(
                x=[x[k]], y=[y[k]], z=[z[k]],
                mode='markers',
                marker=dict(size=5, color=colors[i % len(colors)]),
                name=name
            ))
        frames.append(go.Frame(data=frame_data))

    data_initial = []
    for i, (name, (x, y, z)) in enumerate(positions.items()):  #data for figure
        data_initial.append(go.Scatter3d(
            x=[x[0]], y=[y[0]], z=[z[0]],
            mode='markers',
            marker=dict(size=5, color=colors[i % len(colors)]),
            name=name
        ))


    u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j] # earth surface
    earth_x = 6371 * np.cos(u) * np.sin(v)
    earth_y = 6371 * np.sin(u) * np.sin(v)
    earth_z = 6371 * np.cos(v)
    earth = go.Surface(x=earth_x, y=earth_y, z=earth_z, colorscale="Blues", opacity=0.6, showscale=False)


    fig = go.Figure(         # figure
        data=data_initial+[earth]+orbit_lines,
        frames=frames,
        layout=go.Layout(
            title="Satellite Orbit Animation",
            scene=dict(
                xaxis=dict(range=[-10000, 10000]),
                yaxis=dict(range=[-10000, 10000]),
                zaxis=dict(range=[-10000, 10000])
            ),
            updatemenus=[dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(label="Play", method="animate",
                        args=[None, {"frame": {"duration": 200, "redraw": True},
                                    "fromcurrent": True, "transition": {"duration": 0}}]),
                ]
            )]
        )
    )

    st.plotly_chart(fig)

