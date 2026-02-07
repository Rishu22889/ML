from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model with proper path handling
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["cgpa"]),
        float(request.form["internships"]),
        float(request.form["projects"]),
        float(request.form["certifications"]),
        float(request.form["aptitude"]),
        float(request.form["softskills"]),
        float(request.form["extracurricular"]),
        float(request.form["placetrain"]),
        float(request.form["ssc"]),
        float(request.form["hsc"]),
    ]
    X = np.array(features).reshape(1, -1)
    x = (features[1]+features[2]+features[3])/3
    X = np.hstack((X, [[x]]))
    prob = model.predict_proba(X)[0][1]

    result = "Likely Placed" if prob>0.5 else "Not Likely Placed"

    return render_template(
        "index.html",
        prediction = result,
        probability = round(prob * 100, 2)
    )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
