from flask import Flask, request ,render_template, jsonify
#from sklearn.externals import joblib
import traceback
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__,static_url_path='/static')
model = joblib.load("random_forest.joblib")
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
   values = [ ]
   final_features = [float(x) for x in request.form.values()]
   print(final_features)
   values.append(final_features[0]) #month
   print(values)
   values.append(final_features[1]) #weekday (day of a week)
   values.append((final_features[2])) #humidity
   values.append((final_features[3])) #Temperature
   values.append((final_features[4])) #Windspeed
   if (final_features[5] == 1):          # encoded values for season
      values.append(1)
      values.append(0)
      values.append(0)
      values.append(0)
   elif (final_features[5] == 2):
      values.append(0)
      values.append(1)
      values.append(0)
      values.append(0)
   elif (final_features[5] == 3):
      values.append(0)
      values.append(0)
      values.append(1)
      values.append(0)
   elif (final_features[5] == 4):
      values.append(0)
      values.append(0)
      values.append(0)
      values.append(1)
          
   if (final_features[6] == 0):          # encoded values for holiday
      values.append(1)
      values.append(0)
   elif (final_features[6] == 1):
      values.append(0)
      values.append(1)
        
   if (final_features[7] == 0):          # encoded values for workingdays or weekend
      values.append(1)
      values.append(0)
   elif (final_features[7] == 1):
      values.append(0)
      values.append(1) 
	  
   if (final_features[8] == 1):          # encoded values for season
      values.append(1)
      values.append(0)
      values.append(0)
   elif (final_features[8] == 2):
      values.append(0)
      values.append(1)
      values.append(0)
   elif (final_features[8] == 3):
      values.append(0)
      values.append(0)
      values.append(1)
          
   if (final_features[9] == 0):          # encoded values for workingdays or weekend
      values.append(1)
      values.append(0)
   elif (final_features[9] == 1):
      values.append(0)
      values.append(1)
   print(values)
   prediction = model.predict([values])
   print(prediction)
   return render_template('index.html', prediction_text='Demand is {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
