# The above code is of task-3 using LSTM<br>
## Description:<br>  
- Fetches satellite position data (x, y, z in km) at fixed time intervals using Skyfield.  
- Creates a sliding window dataset (sequence of 10 previous positions → next position).  
- Trains an LSTM model for sequence-to-point regression.  
- Evaluates performance using RMSE and compares predicted vs actual positions.
- Plot the error using Plotly.<br>
### By<br>
-Yeeshika
  
