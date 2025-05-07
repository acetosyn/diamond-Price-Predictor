from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('diamond_model.pkl', 'rb') as f:
    lr = pickle.load(f)

@app.route('/')
def home():
    return render_template('diamond.html')

@app.route('/predict', methods=['POST'])
def predict_price():
    try:
        # Handle JSON request (from JS)
        if request.is_json:
            data = request.get_json()
            carat = float(data['carat'])
            cut = int(data['cut'])
            clarity = int(data['clarity'])
            color = int(data['color'])

            X = np.array([[carat, cut, clarity, color]])
            prediction = lr.predict(X)[0]
            pred_price = round(prediction, 2)

            return jsonify({'price': f"${pred_price}"})
        
        # Fallback to form submission (if needed)
        else:
            carat = float(request.form['carat'])
            cut = int(request.form['cut'])
            clarity = int(request.form['clarity'])
            color = int(request.form['color'])

            X = np.array([[carat, cut, clarity, color]])
            prediction = lr.predict(X)[0]
            pred_price = round(prediction, 2)

            return render_template('diamond.html', pred=f"${pred_price}")

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
