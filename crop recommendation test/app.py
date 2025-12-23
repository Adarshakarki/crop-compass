import pickle
import numpy as np
# Added session, redirect, and url_for
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
# --- IMPORTANT: Set a secret key for session management ---
# You MUST change this key to a strong, random value for production!
app.secret_key = 'your_strong_secret_key_12345' 

# ---------------- LOAD MODEL ----------------
MODEL_PATH = "models/crop_model.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model, scaler, label_encoder = pickle.load(f)
    print("✅ Model, scaler, and label encoder loaded successfully!")
except FileNotFoundError:
    print(f"❌ Error: Model file not found at {MODEL_PATH}")
    model, scaler, label_encoder = None, None, None
except Exception as e:
    print(f"❌ Error loading model components: {e}")
    model, scaler, label_encoder = None, None, None


# ---------------- HOME ----------------
@app.route("/")
def home():
    """
    Renders the main form page. Retrieves prediction from session for persistence.
    """
    # Retrieve the prediction from the session and remove it immediately.
    # This keeps it persistent for one refresh, then clears it for a new session.
    prediction = session.pop('prediction', None)
    
    # Pass the prediction (or None) to the template
    return render_template("index.html", prediction=prediction)

# ---------------- PREDICT ----------------
@app.route("/predict", methods=["POST"])
def predict():
    """
    Processes the prediction request, stores the result in session, and redirects (PRG pattern).
    """
    # Clear any previous attempt from the session
    session.pop('prediction', None) 
    
    if model is None or scaler is None or label_encoder is None:
        session['prediction'] = "Error: Model components failed to load."
        return redirect(url_for('home'))

    try:
        # Read inputs from form (order MUST match training)
        features = [
            float(request.form["boron"]),
            float(request.form["clay"]),
            float(request.form["nitrogen"]),
            float(request.form["organic"]),
            float(request.form["k"]),
            float(request.form["p2o5"]),
            float(request.form["ph"]),
            float(request.form["sand"]),
            float(request.form["slit"]),
            float(request.form["zinc"]),
            float(request.form["avg_temp"]),
            float(request.form["avg_rain"]),
        ]

        # Convert to array and scale
        X = np.array(features).reshape(1, -1)
        X_scaled = scaler.transform(X)

        # Predict and decode
        pred_encoded = model.predict(X_scaled)
        crop = label_encoder.inverse_transform(pred_encoded)[0]

        # Store the successful prediction result in the session
        session['prediction'] = crop
        
        # --- PRG PATTERN: Prevents "Do you want to resubmit?" ---
        return redirect(url_for('home'))

    except Exception as e:
        # Store the error message in the session
        session['prediction'] = f"Error: Please ensure all fields are filled correctly. Details: {e}"
        # Redirect to home to display the error
        return redirect(url_for('home'))

# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)