Live link: https://generativetask2deploy-yeetv8xkdvyxr4djcxjwjzrjf.streamlit.app/  <br>
### Overview 
This project visualizes the 3D orbital trajectories of 10 satellites around Earth over the past 30 days. Using real-world Two-Line Element (TLE) data, it calculates satellite positions at regular intervals and animates their movement in an interactive 3D plot. The visualization satellites using distinct colors and shows their orbits alongside the Earth. 
### Approach 
  -> Data Collection:<br> 
    Selected 10 satellites from various categories (NOAA, GPS, Scientific, Communication).<br> 
    Obtained their TLE data from public sources (CelesTrak, NORAD).<br> 
    TLE data provides orbital elements required to compute satellite positions at any given time.<br> 
  -> Position Calculation:<br> Used the Skyfield library to parse TLE data and compute satellite positions.<br>
    Calculated positions at 3-hour intervals over the past 30 days.<br> 
    Converted satellite positions to 3D Cartesian coordinates (x, y, z in km).<br> 
  -> 3D Visualization<br> 
    Used Plotly to create 3D scatter plots and line traces.<br> 
    Rendered Earth as a semi-transparent 3D surface using spherical coordinates.<br>
    Satellite orbits drawn as lines, while moving satellites represented as markers.<br> 
  -> Animation<br> 
    Generated frames for each time step.<br> 
    Each frame contains markers for all satellites at that timestamp.<br> 
    Added Play button for continuous animation using Plotly’s animation functionality.<br> 
  -> Deployment<br> 
    Wrapped the application in a Streamlit web app for interactive deployment.<br> 
    Users can click a button to load and animate satellite trajectories.<br>
