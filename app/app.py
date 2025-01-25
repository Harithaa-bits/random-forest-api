from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Adjusted path for loading the model
model_path = os.path.join(os.getcwd(), 'models', 'random_forest_model.pkl')
model = joblib.load(model_path)

@app.route("/")
def home():
    return "Random Forest Model API"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Parse JSON input
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)

        # Prediction
        prediction = model.predict(features).tolist()
        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
