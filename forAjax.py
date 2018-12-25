import json
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)


@app.route("/")
def html():
    return render_template('ajaxtest.html')

@app.route("/111",methods=['POST'])
def ajax_demo():
    print(request.form['usrname'])
    print(request.form['groupname'])
    print(request.form['projectname'])
    id=0
    TIME=os.time
    NAME=request.form['usrname']
    RGROUP=request.form['groupname']
    RNAME=request.form['projectname']
    PCOUNT=1
    ISFINISHED=0

    # if request.method == 'POST':
    #     ret = {'status':False,'message':''}
    #     print("hahahaha")
    #
    #     \ssjshh\sss

app.run()