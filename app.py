from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(name)
model = joblib.load("model.pkl") # Load your model

@app.route("/")
def home():
 return "OTP Fraud Detection API is running!"

@app.route("/predict", methods=["POST"])
def predict():
 try:
  data = request.get_json()
  df = pd.DataFrame([data])
  prediction = model.predict(df)[0]
  message = "⚠️ Fraudulent OTP detected. Do NOT share this code!"
if prediction == 1 else "✅ OTP seems genuine."
    return jsonify({"prediction": int(prediction), "message": message})
 except Exception as e:
    return jsonify({"error": str(e)})

if name == "main":
app.run()
