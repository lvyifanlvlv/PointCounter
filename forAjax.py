import json
from flask import Flask, render_template, request, jsonify
import time
from jishu import entrance

app = Flask(__name__)


@app.route("/")
def html():
    return render_template('ajaxtest.html')

@app.route("/111",methods=['POST'])
def ajax_demo():
    print(request.form['usrname'])
    print(request.form['groupname'])
    print(request.form['projectname'])
    new_dict = {}
    new_dict['ID'] = "thresholdtest.png"
    new_dict['TIME'] = time.time()
    new_dict['NAME'] = request.form['usrname']
    new_dict['RGROUP'] = request.form['groupname']
    new_dict['RNAME'] = request.form['projectname']
    new_dict['PCOUNT'] = 1
    new_dict['ISFINISHED'] = 0
    new_dict['B_CNT'] = 0
    new_dict['G_CNT'] = 0
    print("hahaha")
    f=open("myjson/receive.json", "w")
    json.dump(new_dict, f)
    f.close()
    entrance.ent()
    print("12")
    # if request.method == 'POST':
    #     ret = {'status':False,'message':''}
    #     print("hahahaha")
    #
    #     \ssjshh\sss

app.run(
      port= 2300,
      debug=True
)