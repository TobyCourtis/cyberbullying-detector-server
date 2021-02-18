import sys
import pandas as pd
from flask import Flask, render_template, request, redirect, Response, url_for, json
import pickle
import numpy as np
import json
from scipy.sparse.linalg import svds
from flask_sslify import SSLify
from flask_talisman import Talisman
from string import punctuation

if(len(sys.argv) == 2):
    if(sys.argv[1] == "SSL"):
        print("Using SSL")
        use_ssl = True
    else:
        print("\nInvalid parameter found, use 'SSL' or no parameters\n")
        sys.exit(1)
else:
    use_ssl = False
    print("Not using SSL")

# classifier file name here
filename = "./data/classifiers/classifier_combined_data_json80.sav"

loaded_model = pickle.load(open(filename, 'rb'))

print("loading vectors...")
with open('./data/vectors/index_map.pkl', 'rb') as f:
    index_map = pickle.load(f)

vectors2 = np.load("./data/vectors/vectors-float32.npz")
vectors = vectors2['arr_0'][:]
print("Done loading vectors... ")


def sentence(toUse):
    text = toUse.split()
    sentence_vector = np.zeros(300, dtype=np.float32)
    for word in text:
        try:
            word = word.strip(punctuation)
            sentence_vector += vectors[index_map[word]]
        except:
            pass
    sentence_vector /= len(text)
    return list(sentence_vector)

app = Flask(__name__)
if(use_ssl):
    Talisman(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/')
def output():
    return render_template("main.html", classification="Nothing has been input for classification")


@app.route('/classify',methods = ['POST'])
def tester():
    if request.method == 'POST':
        classify_text = request.form['classify_text']
        input_to_classify = np.array(sentence(classify_text))
        test = np.reshape(input_to_classify,(1,-1))
        if loaded_model.predict(test)[0] == 1:
            classify = "Bullying Detected"
        else:
            classify = "No Bullying Detected"
        return render_template("main.html", classification=classify)

@app.route('/classify_js',methods = ['POST'])
def js_classify():
    if request.method == 'POST':
        data = request.get_json()
        try:
            classify_text = data['classify_text']
            classify_text = classify_text.lower()
            input_to_classify = np.array(sentence(classify_text))
            test = np.reshape(input_to_classify, (1, -1))
            if loaded_model.predict(test)[0] == 1:
                classify = {"classification":"Classification: Bullying Detected"}
            else:
                classify = {"classification":"Classification: No Bullying Detected"}
        except:
            classify = {"classification":"Classification: No input has been detected for classification"}
        response = app.response_class(
            response=json.dumps(classify),
            status=200,
            mimetype='application/json'
        )
        return response

@app.route('/classify_binary',methods = ['POST'])
def js_binary():
    if request.method == 'POST':
        data = request.get_json()
        try:
            classify_text = data['classify_text']
            classify_text = classify_text.lower()
            input_to_classify = np.array(sentence(classify_text))
            test = np.reshape(input_to_classify, (1, -1))
            if loaded_model.predict(test)[0] == 1:
                # bullying detected
                classify = 1
            else:
                # no bullying detected
                classify = 0
        except:
            classify = 666
        response = app.response_class(
            response=json.dumps(classify),
            status=200,
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    if(use_ssl):
        # use "0.0.0.0" to host from server IP
        app.run(use_reloader=False,host="127.0.0.1",port=8080,ssl_context=("./ssl_certificates/cert.pem","./ssl_certificates/key.pem"),debug=False)
    else:
        app.run("127.0.0.1", "8080")
