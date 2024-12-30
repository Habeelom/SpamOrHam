from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('logistic_regression.pkl', 'rb'))
feature_extraction = pickle.load(open('feature_extraction.pkl', 'rb'))

def predict_mail(input_text):
    input_features = feature_extraction.transform([input_text])
    prediction = model.predict(input_features)
    return prediction[0]

@app.route('/', methods=['GET', 'POST'])
def analyze_mail():
    if request.method == 'POST':
        mail_content = request.form.get('mail')
        if mail_content:
            prediction = predict_mail(mail_content)
            return render_template('index.html', classify=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)