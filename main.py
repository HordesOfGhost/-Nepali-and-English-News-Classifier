from flask import Flask, request, render_template
from backend.classify import Predict_news

from backend.calculatetfidf import ProcessText,calc_tf_idf
app = Flask(__name__)

@app.route('/')
def bbc_form():
    return render_template('BBCForm.html')

@app.route('/', methods=['POST'])
def recieve_text():
    text = request.form['news']
    prediction,confidence=Predict_news(text)
    return render_template("BBCForm.html",prediction=prediction,confidence=confidence,text=text)



if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
            