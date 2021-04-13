# Project - SherLock
Sherlock vs Moriarty: A smartphone dataset for cybersecurity research.


This project will look into applying a faux regression to capture the Moriarty actions.  The data can be found at <link broken, Dave?> [Project Website](http://bigdata.ise.bgu.ac.il/sherlock/) or a 2 week subset on [Kaggle](https://www.kaggle.com/BGU-CSRC/sherlock). 

A paper discussing this dataset can be found at [Mirsky et al.](https://dl.acm.org/doi/pdf/10.1145/2996758.2996764?casa_token=E9wxVhbwsz8AAAAA:uSv_OH8chsX91Ei1DSNmN9jGT9uyfwdccrj2ix6P2D09377jjD7OTGzO0pEvU5Vf0N-iaSg7BgBcyg).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries.

```bash
pip install -r requirements.txt
```

## Usage
The current state of this project and mini-assignments walks through data-loading, a sample EDA, then a faux-linear regression modeling and pickle'ing.  A standalone python script will then run the pickled model.

From a command line within this project directory, type:

``` jupyter notebook ```

The fitting of the model is performed in the Jupyter notebook, 'SherLock.ipynb'.  A pickled model will be generated and a python script, 'test_pickled_model.py' will perform a faux-prediction using the command

``` python test_pickled_model.py ``` 

on the command line. 

## Web shenagans with Flask

Flask will be used to (localy) share the fun.  

## Usage:
Type 'FLASK_APP=app.py' and 'FLASK_ENV=development' on the terminal commandline within the activated python environment.  Then 'flask run'.  Open browser and go to flask address/port, something like 'http://127.0.0.1:5000'  To run the prediction with JSON data, type 'python test_flask.py'.  The results should like: 
```[[970.4839983746325], [968.4961539698425]]```


Enjoy!
