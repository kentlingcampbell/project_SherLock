from flask import Flask, request
import pickle

app = Flask(__name__)

# Import model pickle
with open('model.pkl', 'rb') as f:
    pipePKL = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata = the_data['newdata']
        prediction = pipe.predict([newdata])
        return {'Good day to you. The prediction for the data is' : prediction.tolist()}
    else:
        return {'Yo!  Dude!'}
