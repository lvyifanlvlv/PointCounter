import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/html")
def html():
    return render_template('ajaxtest.html')

@app.route("/111",methods=['POST'])
def ajax_demo():
    print("aaaa")
    print(request.form['a'])
    print(request.form['b'])
    print(request.form['c'])
    # if request.method == 'POST':
    #     ret = {'status':False,'message':''}
    #     print("hahahaha")
    #
    #     \ssjshh\sss

app.run()