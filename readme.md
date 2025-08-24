    <---------- TRAJECTORY ANIMATION OF THR SATELLITE FOR 30 DAYS ----------->

    
____first of all i inluceded and imported all the libraries and functions which was required in the entire coding which are as follows:
**streamlit**(primarily used for rapid building and sharing interactive web applications without any knowledge of HTML,CSS,JAVASCRIPT especially in the field of data science and machine learining etc .),_______



______**skyfiled**(contains all the necessary and essential functions which are required for the astronomical analysis such as position of celestial bodies ,earth satellites etc)



_____then i imported 
**numpy**:(used for dealing with the data and computations of the numerical data in the vector,matrix and tensor format etc )_____

_____**plotly**(: it is basically used for generating dynamic and interactive charts )_____




_____**ts=load.timescale()**  defined timescale ______




______provided tle_data in the list with tle_data_____



_______satellite=[] , created empty list for fetching the data of tles as line1,line2 ,name ,ts_____



_______created for loop for appendinmg tles data into just created list named as satellite ______


_______defined number of days ______


______tuples of 24 hours ______



_______defined a universal time that is utc ______



______for loop for fetching positions x,y,z______



_______deined colors_list for the identification of different-different satellites______



_______curve for the orbit ________



_____animation by .goscatter _____


________Streamlit Integration :Displayed the 3D animation inside a web app______

