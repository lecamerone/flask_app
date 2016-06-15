from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.config['DEBUG']=True
@app.route("/")
def index():
	return 'Hello world'

from flask import jsonify
from pandasfin import pandas_google_fin
import pandas.io.data as web
import pandas as pd
import datetime
from flask import jsonify
 

start = datetime.datetime(2016,5,13)
end = datetime.datetime(2016,6,14)
f = jsonify(pandas_google_fin(start,end))
@app.route("/data")
def data_show():
	return render_template('open_close.html', json_file=f)

if __name__ == "__main__":
	app.run()