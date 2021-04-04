# test_pickled_model.py

newdata = ____ # load your newdata, see sections above...

pipe = ____ # unpickle the pipe...

# `model.predict` and friends expect a 2-d array of data. If your newdata is
# one-dimensional, make it two-dimensional by wrapping it in a list.
# numpy can be used to check the number of dimensions of a list.
#    
#    import numpy as np
#    newdata = np.array(newdata)
#    if newdata.ndim == 1:
#        newdata = [newdata]

predictions = pipe.predict_proba(newdata)
print(predictions)
