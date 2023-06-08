from flask import Flask, escape, request, render_template
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
scaler = StandardScaler()

model = pickle.load(open("Stroke_model.pkl", 'rb'))

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/collect_data')
def collect_data():
    return render_template('data.html')


@app.route('/result', methods=['POST', 'GET'])
def predict():
    if request.method =="POST":
        gender = request.form['gender']
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        disease = int(request.form['heart_disease'])
        glucose = float(request.form['avg_glucose_level'])
        smoking = request.form['smoking_status']

        # gender
        gender_male, gender_female = 0,0
        if (gender == "Male"):
            gender_male=1
        elif(gender == "Female"):
            gender_female = 1
        
        

        # smoking status
        never_smoked, formely_smoked = 0,0
        if(smoking=='never smoked'):
            never_smoked = 1
        elif smoking=='formerly smoked':
            formely_smoked = 1

        X  = np.array([gender_male, gender_female, age, hypertension, disease, glucose, formely_smoked, never_smoked])
        # feature = scaler.fit_transform([X])
        print(X)

        prediction = model.predict([X])[0]

        return render_template("result.html", prediction_text=prediction) 
    else:
        return render_template("result.html")  





if __name__ == "__main__":
    app.run(debug=True)