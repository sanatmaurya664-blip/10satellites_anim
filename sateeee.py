import streamlit as st
from skyfield.api import load, EarthSatellite
import numpy as np
import plotly.graph_objects as go
st.title("3D Satellite Orbit Animation")

ts = load.timescale()

tle_data = [
    ("1 25544U 98067A   25229.18034946  .00009619  00000+0  17645-3 0  9995",
     "2 25544  51.6356   4.7550 0003499 229.5075 130.5609 15.49975761524621",
     "ISS (ZARYA)"),
    ("1 20580U 90037B   25229.99494465  .00005450  00000+0  19821-3 0  9991",
     "2 20580  28.4692 345.7803 0002448  54.4458 305.6364 15.25933490742399",
     "HST"),
    ("1 44714U 19074B   25229.75455862  .00000837  00000+0  75090-4 0  9995",
     "2 44714  53.0568  22.1224 0001218  92.2944 267.8185 15.06398676318015",
     "STARLINK-1008"),
    ("1 24946U 97051C   25229.76631521  .00000231  00000+0  74396-4 0  9996",
     "2 24946  86.3874 117.3430 0006055 227.8565 132.2118 14.34924897461575",
     "IRIDIUM 33"),
    ("1 04793U 70106A   25229.92380204 -.00000053  00000+0 -64873-4 0  9996",
     "2 04793 101.3854 272.2918 0031288 220.6116 312.7732 12.54044439502679",
     "NOAA 1"),
    ("1 22490U 93009B   25230.18410895  .00000425  00000+0  65562-4 0  9994",
     "2 22490  24.9692 278.1444 0042088 171.1063 226.4079 14.45888210717615",
     "SCD 1"),
    ("1 27848U 03031J   25229.94062835  .00000238  00000+0  12400-3 0  9995",
     "2 27848  98.6807 237.2774 0009727  11.3414 348.7982 14.23370635148233",
     "CUBESAT XI-IV (CO-57)"),
    ("1 22675U 93036A   25229.89482750  .00000079  00000+0  38359-4 0  9993",
     "2 22675  74.0399 169.3638 0025964 281.7921  78.0318 14.33157476680998",
     "COSMOS 2251"),
    ("1 39418U 13066C   25230.11996940  .00002227  00000+0  13866-3 0  9991",
     "2 39418  97.4295 283.8382 0021018 281.1697  78.7170 15.10427150642696",
     "SKYSAT-A"),
    ("1 25730U 99025A   25230.16340779  .00001186  00000+0  52400-3 0  9990",
     "2 25730  98.8982 294.5964 0010808  46.2529 313.9543 14.25171470355112",
     "FENGYUN 1C"),
]


satellites = []
for line1, line2, name in tle_data:
    satellites.append(EarthSatellite(line1, line2, name, ts))

num_days = 31
hours = np.arange(0, 24, 1)
all_times = ts.utc(
    2025, 8,
    np.repeat(np.arange(1, num_days + 1), len(hours)),
    0,
    np.tile(hours, num_days)
)
positions_x, positions_y, positions_z = [], [], []
for sat in satellites:
    pos = sat.at(all_times).position.km
    x, y, z = pos
    positions_x.append(x)
    positions_y.append(y)
    positions_z.append(z)
color_list = [
    "red", "blue", "green", "orange", "purple",
    "cyan", "magenta", "yellow", "pink", "brown"
]
orbit_traces = []
for idx in range(len(satellites)):
    orbit_traces.append(
        go.Scatter3d(
            x=positions_x[idx],
            y=positions_y[idx],
            z=positions_z[idx],
            mode="lines",
            line=dict(color=color_list[idx], width=1),
            name=f"{satellites[idx].name} Orbit",
            opacity=0.4
        )
    )
frames = []
for t_idx in range(len(all_times)):
    frame_objs = []
    for s_idx in range(len(satellites)):
        frame_objs.append(
            go.Scatter3d(
                x=[positions_x[s_idx][t_idx]],
                y=[positions_y[s_idx][t_idx]],
                z=[positions_z[s_idx][t_idx]],
                mode="markers",
                marker=dict(size=6, color=color_list[s_idx]),
                name=satellites[s_idx].name
            )
        )
    frames.append(go.Frame(data=frame_objs))
init_points = []
for s_idx in range(len(satellites)):
    init_points.append(
        go.Scatter3d(
            x=[positions_x[s_idx][0]],
            y=[positions_y[s_idx][0]],
            z=[positions_z[s_idx][0]],
            mode="markers",
            marker=dict(size=4, color=color_list[s_idx]),
            name=satellites[s_idx].name
        )
    )
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
earth_x = 6371 * np.cos(u) * np.sin(v)
earth_y = 6371 * np.sin(u) * np.sin(v)
earth_z = 6371 * np.cos(v)
earth_surface = go.Surface(
    x=earth_x, y=earth_y, z=earth_z,
    colorscale="Blues", opacity=0.6, showscale=False
)
fig = go.Figure(
    data=init_points + [earth_surface] + orbit_traces,
    layout=go.Layout(
        title="Satellite Orbits Around Earth (Animated)",
        scene=dict(
            xaxis=dict(range=[-10000, 10000]),
            yaxis=dict(range=[-10000, 10000]),
            zaxis=dict(range=[-10000, 10000])
        ),
        updatemenus=[
            dict(
                type="buttons", showactive=False,
                buttons=[
                    dict(
                        label="Play", method="animate",
                        args=[None, {"frame": {"duration": 500, "redraw": True},
                                     "fromcurrent": True, "transition": {"duration": 0}}]
                    ),
                    dict(
                        label="Pause", method="animate",
                        args=[[None], {"frame": {"duration": 0, "redraw": False},
                                       "mode": "immediate",
                                       "transition": {"duration": 0}}]
                    )
                ]
            )
        ]
    ),
    frames=frames
)
st.plotly_chart(fig, use_container_width=True)
