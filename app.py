from flask import Flask, request, jsonify
import pickle


app = Flask(__name__)

# Import model pickle
with open('model.pkl', 'rb') as f:
    pipe = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        the_data = request.get_json(force=True)
        newdata = the_data['newdata']
        prediction = pipe.predict(newdata)
        return jsonify(prediction.tolist())
    else:
        return {'Yo!  Dude!'}
