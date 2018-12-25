import json
from flask import Flask, render_template, request, jsonify
import time
from jishu import entrance
import os

app = Flask(__name__)


@app.route("/")
def html():
    return render_template('/counter/app/views/counters/ajaxtest.html')

@app.route('/111',methods=['POST','GET'])
def test_json():
    #获取JSON数据
    img=request.form.get('img')
    img1="templates/counter/public"+img[0:28]
    for filename in os.listdir(r"%s"%img1):              #listdir的参数是文件夹的路径
    	img1=img1+filename
    print(img1)
    ktz=request.form.get('studentnumber')
    name=request.form.get('studentname')
    pjn=request.form.get('projectname')
    new_dict = {}
    new_dict['ID'] = img1
    new_dict['TIME'] = time.time()
    new_dict['NAME']=name
    new_dict['RGROUP']=ktz
    new_dict['RNAME']=pjn
    new_dict['PCOUNT']=1
    new_dict['ISFINISHED']=0
    new_dict['B_CNT']=0
    new_dict['G_CNT']=0
    f=open("myjson/receive.json","w")
    json.dump(new_dict,f)
    f.close()
    entrance.ent()
    f1=open("myjson/return.json",'r')
    load_dict=json.load(f1)
    G_num=load_dict['B_CNT']
    B_num=load_dict['G_CNT']
    #返回
    return jsonify({'green':G_num,'blue':B_num})


app.run(
      host='0.0.0.0',
      port= 2300,
      debug=True
)
