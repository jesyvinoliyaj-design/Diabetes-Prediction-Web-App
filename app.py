from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model & scaler
model = pickle.load(open('diabetes_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Handle JSON request
    if request.is_json:
        data = request.get_json()
        features = [
            data['Pregnancies'],
            data['Glucose'],
            data['BloodPressure'],
            data['SkinThickness'],
            data['Insulin'],
            data['BMI'],
            data['DiabetesPedigreeFunction'],
            data['Age']
        ]
        final_input = scaler.transform([features])
        prediction = model.predict(final_input)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return jsonify({"prediction": result})
    
    # Handle form request (HTML form)
    else:
        data = [float(x) for x in request.form.values()]
        final_input = scaler.transform([data])
        prediction = model.predict(final_input)[0]
        result = "Diabetic" if prediction == 1 else "Not Diabetic"
        return render_template('index.html', prediction_text=f"Prediction: {result}")

if __name__ == '__main__':
    app.run()
