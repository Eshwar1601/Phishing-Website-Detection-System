from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

# Load the trained model
phish_model_ls = pickle.load(open('phishing.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get("url")  
    
    if not url:
        return jsonify({"error": "Please enter a URL"}), 400  
    
    
    X_predict = [str(url)]
    
    # Predict using the model
    y_Predict = phish_model_ls.predict(X_predict)[0]  # Get single value
    
    # Determine result based on prediction
    result = "This is a Phishing Site" if y_Predict == 'bad' else "This is not a Phishing Site"
    
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000, threaded=True)
