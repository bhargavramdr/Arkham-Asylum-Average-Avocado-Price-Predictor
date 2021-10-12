from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn

model = pickle.load(open("model.pkl", "rb"))


app = Flask(__name__)


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year = float(request.form['year'])

        # Present_Price = float(request.form['Present_Price'])
        # Kms_Driven = int(request.form['Kms_Driven'])
        # Kms_Driven2 = np.log(Kms_Driven)
        # Owner = int(request.form['Owner'])
        region = request.form['region']
        if(region == 'Albany'):
            region = 0.
        elif(region == "Atlanta"):
            region = 1.
        elif(region == 'BaltimoreWashington'):
            region = 2.
        elif(region == "Boise"):
            region = 3.
        elif(region == 'Boston'):
            region = 4.
        elif(region == "BuffaloRochester"):
            region = 5.
        elif(region == "California"):
            region = 6.
        elif(region == 'Charlotte'):
            region = 7.
        elif(region == "Chicago"):
            region = 8.
        elif(region == 'CincinnatiDayton'):
            region = 9.

        type = request.form['type']
        if(type == 'conventional'):
            type = 0.
        else:
            type = 1.

        Total_Volume = float(request.form['Total_Volume'])
        Total_Bags = float(request.form['Total_Bags'])

        prediction = model.predict(
            [[year, region, type, Total_Volume, Total_Bags]])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="Average avocado price in the region is {} dollars".format(output))


if __name__ == "__main__":
    app.run(debug=True)
