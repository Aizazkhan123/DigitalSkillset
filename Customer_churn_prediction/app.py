# save this as app.py
from flask import Flask, escape, request, render_template
import numpy as np
import pickle
model = pickle.load(open('model.pkl', 'rb'))

# model = xgb.Booster()
# model.load_model("model.txt")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analysis')
def analysis():
    return render_template("churn.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        CreditScore=int(request.form['CreditScore'])
        Geography=request.form['Geography']
        Gender=request.form['Gender']
        Age=float(request.form['Age'])
        Tenure=float(request.form['Tenure'])
        Balance=float(request.form['Balance'])
        NumOfProducts=int(request.form['NumOfProducts'])
        HasCrCard=int(request.form['HasCrCard'])
        IsActiveMember=int(request.form['IsActiveMember'])
        EstimatedSalary=float(request.form['EstimatedSalary'])
    
    
     # region_category
        if   Geography== "France":
            Geography= 0
        elif  Geography== "Spain":
            Geography=2
        else:
            Geography=1


        # gender
        if Gender=="Female":
            Gender= 1

        elif Gender=="Male":
            Gender = 0
        
        prediction = model.predict([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])
        # print(prediction)
        if prediction == [1]:
            prediction="Curn"
        else:
            prediction="Not churn"
           



                
        return render_template("prediction.html", prediction_text="Result={}".format(prediction))        

    else:
        return render_template("prediction.html")


if __name__ == "__main__":
    app.run(debug=True)
