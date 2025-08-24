    <---------- TRAJECTORY ANIMATION OF THR SATELLITE FOR 30 DAYS ----------->

    
first of all i inluceded and imported all the libraries and functions which was required in the entire coding which are as following:
**streamlit**(primarily used for rapid building and sharing interactive web applications without any knowledge of HTML,CSS,JAVASCRIPT especially in the field of data science and machine learining etc .),**skyfiled**(contains all the necessary and essential functions which are required for the astronomical analysis such as position of celestial bodies ,earth satellites etc)
then i imported **numpy**:(used for dealing with the data and computations of the numerical data in the vector,matrix and tensor format etc )

**plotly**(: it is basically used for generating dynamic and interactive charts )
**ts=load.timescale()**  defined timescale 
provided tle_data in the list with tle_data
satellite=[] , created empty list for fetching the data of tles as line1,line2 ,name ,ts
created for loop for appendinmg tles data into just created list named as satellite 
defined number of days 
tuples of 24 hours 
defined a universal time that is utc 
for loop for fetching positions x,y,z
deined colors_list for the identification of different-different satellites
curve for the orbit 
animation by .goscatter 
Streamlit Integration :Displayed the 3D animation inside a web app
