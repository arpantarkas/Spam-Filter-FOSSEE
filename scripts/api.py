from flask import Flask, abort, request, jsonify
from sklearn.externals import joblib
import numpy as np
from train_script import lemmatise

app = Flask(__name__)
clf = joblib.load('/model/Trained-Model.pkl')

@app.route('/api', methods=['POST'])
def predict_text():
    data = request.get_json()
    print('Data Recieved :- {}'.format(data))
    predict_text = np.array([data['Data']])
    pred = clf.predict(predict_text).tolist()
	
    return jsonify(results= pred)

    
if __name__ == '__main__':
	app.run(port=8000, debug=True)
