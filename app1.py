from flask import Flask,request, url_for,redirect, render_template
import joblib
import numpy as np


# We need to Create a application 
app = Flask(__name__,template_folder='templates')
model = joblib.load('Fruit_Label.ml')

# gender	religion	caste	mother_tongue	country	height_cms
#New_data = np.array([[0,2,34,6,19,170]])
#print("At This Preson will get a married",model.predict(New_data))

@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    print(int_features)
    final = np.array([[int_features]])
    print(final)
    predication_fruit = model.predict(final)
    print(predication)
    output='{0:.{1}f}'.format(prediction[0][1], 2)
    return render_template('index.html',pred='In this fruit You will Get a Label\nProbability of label occuring is{}'.format(output))
    

if __name__ == '__main__':
    app.run()