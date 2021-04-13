import requests
import json

# POST
# load the test data
with open('testdata.json', 'r') as f:
    testdata = jason.load(f)

r = requests.post('http://127.0.0.1:5000/predict', json={'newdata': testdata})
#print(r.json())
data = r.json()
prediction = data['prediction']
print(prediction)
