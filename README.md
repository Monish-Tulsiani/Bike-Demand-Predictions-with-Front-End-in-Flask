### BIKE SHARING DEMAND

The purpose of this study is to understand what influences Bike Sharing  and also predict it in order to satisfy demand. This study is based on regression analysis methods.

<b>Software and Libraries:</b>

- Python 2.7 or higher
- NumPy
- Matplotlib
- Scikit Learn
- Pandas
- Flask


<b>Project Structure</b>

This project has four major parts :

<b>ipynb file  - </b>This contains code for our Machine Learning model to predict Bike Sharing based on training data in 'days.csv' file.

<b>app.py -</b> This contains Flask APIs that receives Bike Sharing details through GUI or API calls, computes the precited value based on our model and returns it.

<b>request.py -</b> This uses requests module to call APIs already defined in app.py and dispalys the returned value.

<b>templates -</b> This folder contains the HTML template to allow user to enter Bike Sharing Prediction  detail and displays the predicted result.

- We simplify the model the web application by including 7 features:
  - Temperature
  - Humidity
  - Weather
  - Season
  - Holiday
  - Hour
  - WeekDay
  - Windspeed
  - Year
 
<b>Running the project:</b>

1.Ensure that you are in the project home directory. Create the machine learning model in jupyter lab.

2.This would create a serialized version of our model into a file .joblib

3.Run app.py using below command to start Flask API.
    
 <b>python app.py</b>

By default, flask will run on port 5000.

4.Navigate to URL http://localhost:5000
You should be able to view the homepage.
Enter valid numerical values in all  input boxes and hit Submit.

You should be able to see the predcited vaule on the HTML page!


