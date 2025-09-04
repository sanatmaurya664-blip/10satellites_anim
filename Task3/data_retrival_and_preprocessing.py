from skyfield.api import EarthSatellite, load, utc
from datetime import datetime, timedelta
import numpy as np

ts = load.timescale()

x = []
y = []
z = []
times = []

satellite = """IRIS
            1 39197U 13033A   25231.57687540  .00001065  00000+0  13165-3 0  9994
            2 39197  97.9505  66.6828 0023900 222.8047 137.1307 14.84728440655629"""

tle_lines = [line.strip() for line in satellite.strip().split('\n')]

end_time = datetime.now(tz = utc)    ### 5 days with 10 minutes gap 
start_time = end_time - timedelta(days=5)
delta = timedelta(minutes=10)

sat_info = EarthSatellite(tle_lines[1], tle_lines[2], tle_lines[0], ts)   #EarthSattilite object

while start_time <= end_time :  #list of time
  times.append(ts.utc(start_time))
  start_time += delta



for time in times :
  geo = sat_info.at(time)
  pos = geo.position.km
  x.append(pos[0])
  y.append(pos[1])
  z.append(pos[2])

x = np.array(x)
y = np.array(y)
z = np.array(z)

#print(len(x_train))

features=[]   #last 10 positions
next_pos = []  #current position


for i in range(10, len(x)):
  row = []
  for j in range(i - 10, i):  #previous 10 positions
      row.append(x[j])  
      row.append(y[j])
      row.append(z[j])
  features = features + row   
  next_pos.append(x[i])  #corresponding to previous positions 
  next_pos.append(y[i])
  next_pos.append(z[i])

features = np.array(features).reshape(-1, 30)
next_pos = np.array(next_pos).reshape(-1, 3)
print(features.shape)

np.save("features.npy",dataFrame)
np.save("output.npy",next_pos)

