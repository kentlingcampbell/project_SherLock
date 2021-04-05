# test_pickled_model.py

from newdata import newdata
newdata

import pickle
with open('model.pkl', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    pipePKL = pickle.load(f)

predictions = pipePKL.predict(newdata)
print(predictions)
