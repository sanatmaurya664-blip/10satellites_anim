import numpy as np
from skyfield.api import EarthSatellite, load
import datetime

# Example TLE (ISS)
line1 = "1 25544U 98067A   21275.51041667  .00001264  00000-0  32219-4 0  9993"
line2 = "2 25544  51.6450  21.6475 0004271  20.6810  62.3515 15.48909355306326"
satellite = EarthSatellite(line1, line2, "ISS (ZARYA)")

# Time setup
days = 5
interval_minutes = 5
ts = load.timescale()

# Generate timestamps
start_time = datetime.datetime(2025, 9, 1)
rows = (24 * 60 // interval_minutes) * days
time_stamps = [start_time + datetime.timedelta(minutes=i*interval_minutes) for i in range(rows)]
skyfield_times = ts.utc([t.year for t in time_stamps],
                        [t.month for t in time_stamps],
                        [t.day for t in time_stamps],
                        [t.hour for t in time_stamps],
                        [t.minute for t in time_stamps],
                        [t.second for t in time_stamps])

# Extract satellite positions
geocentric = satellite.at(skyfield_times)
subpoint = geocentric.subpoint()

latitudes = subpoint.latitude.degrees
longitudes = subpoint.longitude.degrees
altitudes = subpoint.elevation.km

# Stack into array
data = np.column_stack((latitudes, longitudes, altitudes))
np.save("tle_data.npy", data)

print(f"Data shape: {data.shape}")
print("Saved file: tle_data.npy")
